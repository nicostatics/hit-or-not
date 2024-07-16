# Import necessary libraries
import pandas as pd

def load_and_combine_data(artist_path, artist_tracks_path, tracks_path, youtube_path):
    # Load each CSV into a DataFrame
    artist_df = pd.read_csv(artist_path)
    artist_tracks_df = pd.read_csv(artist_tracks_path)
    tracks_df = pd.read_csv(tracks_path)
    youtube_df = pd.read_csv(youtube_path)
    
    # Join artist_df with artist_tracks_df on artist ID
    combined_df_1 = pd.merge(artist_df, artist_tracks_df, left_on='id', right_on='cm_artist', how='left')
    
    # Assuming tracks_df contains a column 'track_id' that matches with 'track_id' in artist_tracks_df
    combined_df_2 = pd.merge(combined_df_1, tracks_df, on='cm_track', how='left')
    
    # Assuming youtube_df contains a column 'youtube_track_id' that matches with 'track_id' in tracks_df
    final_combined_df = pd.merge(combined_df_2, youtube_df, left_on='cm_track', right_on='cm_track', how='left')
    
    return final_combined_df

def main():
    # Define paths to the CSV files
    artist_path = '/CSVs/artist_df.csv'
    artist_tracks_path = '/CSVs/artist_tracks_df.csv'
    tracks_path = '/CSVs/tracks_df.csv'
    youtube_path = '/CSVs/youtube_df.csv'
    
    # Combine data from all CSV files
    combined_data = load_and_combine_data(artist_path, artist_tracks_path, tracks_path, youtube_path)
    
    # Save the combined DataFrame to a new CSV file
    combined_data.to_csv('/CSVs/combined_data.csv', index=False)
    print("Data combined and saved to combined_data.csv.")

if __name__ == "__main__":
    main()
