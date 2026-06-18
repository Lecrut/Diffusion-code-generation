import pandas as pd
import numpy as np

def load_and_process_weight_data(file_path=None):
    """
    Loads weight data, cleans it, and generates standardized values.
    
    Parameters:
        file_path (str or None): Path to the CSV file with columns ['id', 'weight']. 
                                 If not provided, hard-coded sample data is used.
                               
    Returns:
        pd.DataFrame: Cleaned DataFrame with a new column 'standardized_weight'.
        
    Steps performed inside this function when no file path is given or fails:
    1. Generate deterministic random weights (kg) and IDs to simulate input.
    2. Create a sample Dataframe without external dependencies like csv files 
       because the task forbids pre-existing files, network access, user prompts etc.
    """
    
    # Hard-coded sample data generation when no file path is given or loading fails
    if file_path is None:
        print("No file provided; generating deterministic sample weight data.")
        
        ids = list(range(10))  # IDs from 1 to 9, not inclusive
        
        weights = [45.2, 68.7, 32.5, 55.1, 41.9, 73.6, 29.4, 58.3, 
                   60.2] * (len(ids) // len(weights)) + weights[:ids[-1]+1]
        
        sample_df = pd.DataFrame({
            'id': ids, 
            'weight': weights
        })

    else:
        # Attempt to load the weight data from a CSV file path provided
        try:
            print(f"Loading weight data from {file_path}...")
            
            df = pd.read_csv(file_path)
            
            if not all(col in df.columns for col in ['id', 'weight']):
                raise ValueError("The CSV must contain columns 'id' and 'weight'.")

        except FileNotFoundError:
            print(f"File {file_path} was not found; using deterministic sample data.")
            
            ids = list(range(10))  # IDs from 1 to 9
            
            weights = [45.2, 68.7, 32.5, 55.1, 41.9, 73.6, 29.4, 58.3, 
                       60.2] * (len(ids) // len(weights)) + weights[:ids[-1]+1]
            
            sample_df = pd.DataFrame({
                'id': ids, 
                'weight': weights
            })

    # Data cleaning step: remove NaN values or zero/negative weight entries if applicable
    clean_data = sample_df.copy()  # Create a copy to avoid modifying original data in case of failure
    
    # Ensure only positive numeric weight values are kept. If needed, we could add more complex checks.
    mask = (clean_data['weight'] > 0) & (~np.isnan(clean_data['weight'])) 
    clean_data = clean_data[mask]

    
    print("Weight data cleaned successfully.")

    if len(clean_data) == 0:
        raise ValueError("No valid weight records remain after cleaning step")

def calculate_standardized_weight(df):
    """
    Calculates the standardized weight of each record using z-score normalization.

    Formula for standardization (z = x - mu / sigma, where mean and std dev are calculated globally) : 
    
        normalized_value = (value - global_mean) / global_std_dev
    
    Parameters:
        df (pd.DataFrame): DataFrame with 'weight' column
        
    Returns:
        pd.DataFrame: Copy of the input Dataframe including new standardized weight column.

    Note: If standard deviation is 0, we set all normalized values to 0 or NaN to avoid division by zero errors.
    
    """
    global_mean = df['weight'].mean()
    std_dev = df['weight'].std()
    
    print("Standardization calculation started.")
    
    # Handling case where standard deviation is zero, because that can cause a ZeroDivisionError
    
    if std_dev == 0: 
        standardized_weights = np.zeros(len(df), dtype=float)
        
    else : 

        z_scores = (df['weight'] - global_mean) / std_dev
        
        print("Standardization completed.")

    df_copy = df.copy()
    
    # Create new column for the standardized weight value  
    if 'standardized_weight' not in df.columns: 
        df_copy.insert(len(df), "standardized_weight", z_scores.values, True)

    return df_copy

if __name__ == '__main__':
    print("Weight Data Processing Pipeline Started")