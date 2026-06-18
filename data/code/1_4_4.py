import pandas as pd
import numpy as np

def load_and_process_weight_data(file_path: str) -> pd.DataFrame:
    """
    Loads weight data from a CSV file, cleans it by removing rows with missing values 
    or non-numeric weights, and creates a new column 'standardized_weight' using Z-score normalization.

    Args:
        file_path (str): Path to the input CSV file containing 'weight' columns.

    Returns:
        pd.DataFrame: Cleaned DataFrame with an added standardized weight column.
    """
    # Load data assuming at least one numeric column named 'weight' or similar
    try:
        df = pd.read_csv(file_path)
        
        # Ensure there is a valid weight column to process
        if not any(col in ['weight', 'Weight'] for col in df.columns):
            raise ValueError("No suitable 'weight' column found in the dataset.")

        # Select and rename columns for clarity (case-insensitive check logic applied below)
        target_col = None
        for col in df.columns:
            if col.lower() == 'weight':
                target_col = col
                break
        
        if target_col is None:
            raise ValueError("Could not identify a weight column.")

        # Extract the specific weight column and ensure it's numeric
        weights_df = pd.DataFrame(df[target_col])
        
        # Convert to float, handling potential non-numeric strings by converting NaNs
        try:
            clean_weights = pd.to_numeric(weights_df.dropna(), errors='coerce')
        except ValueError as e:
            raise RuntimeError(f"Failed to convert weight column to numeric: {e}")

        # Drop rows where the converted weights are still invalid (NaN)
        valid_mask = ~clean_weights.isna()
        
        if not valid_mask.any():
            print("Warning: No valid numerical data found for processing.")
            return pd.DataFrame(columns=df.columns)

        clean_df = df[valid_mask].copy()
        # Ensure the original column name is preserved in the cleaned dataframe before adding new columns
        clean_df[target_col] = clean_weights
        
        # Calculate Z-score normalization: (x - mean) / std
        mean_weight = clean_df[target_col].mean()
        std_weight = clean_df[target_col].std(ddof=0)  # Population standard deviation

        if pd.isna(std_weight):
            raise ValueError("Standard deviation is zero or undefined; cannot normalize.")

        standardized_values = (clean_df[target_col] - mean_weight) / std_weight
        
        # Add the new column to the dataframe
        clean_df['standardized_weight'] = standardized_values.values.astype(float)

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        raise
    
    return clean_df

if __name__ == '__main__':
    # Hard-coded sample data since no external files or user input is allowed.
    # Simulating a CSV structure with columns 'id', 'category', and 'weight'.
    
    sample_data = {
        "id": [1, 2, 3, 4, 5],
        "category": ["A", "B", "C", "D", "E"],
        "weight": [60.5, np.nan, 75.2, 80.0, None] # Includes NaN and string 'None' to test cleaning
    }

    df_sample = pd.DataFrame(sample_data)
    
    # Create a temporary in-memory file path for the sample data since we cannot rely on pre-existing files.
    import io
    
    buffer = io.StringIO()
    df_sample.to_csv(buffer, index=False)
    temp_file_path = "temp_weight_data.csv"

    try:
        processed_df = load_and_process_weight_data(temp_file_path)
        
        print("Data Processing Complete.")
        print("\nOriginal Data:")
        print(df_sample)
        
        print("\nCleaned and Standardized Data:")
        print(processed_df)
        
        # Verify the standardized column properties
        if 'standardized_weight' in processed_df.columns:
            mean_std = processed_df['standardized_weight'].mean()
            std_calc = processed_df['standardized_weight'].std(ddof=0)
            
            print(f"\nVerification:")
            print(f"Mean of original weights (approx): {df_sample['weight'].dropna().mean():.2f}")
            print(f"Std Dev of standardized column: {std_calc:.6f} (Expected ~1)")
    finally:
        # Clean up the temporary file if it was created on disk (though we used StringIO, 
        # this block ensures safety if a real path logic were expanded later)
        import os
        try:
            os.remove(temp_file_path)
        except FileNotFoundError:
            pass  # File might not exist depending on how pandas writes to temp paths in some environments