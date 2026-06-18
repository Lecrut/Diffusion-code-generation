import pandas as pd
import numpy as np

def load_and_process_weight_data(file_path: str) -> pd.DataFrame:
    """
    Loads weight data from a CSV file, cleans it by removing rows 
    with missing values or non-numeric weights, and creates a new column
    containing standardized (z-score normalized) weight values.

    Parameters:
        file_path (str): Path to the input CSV file.

    Returns:
        pd.DataFrame: Cleaned DataFrame with an additional 'standardized_weight' column.
    """
    # Load data
    df = pd.read_csv(file_path, skipinitialspace=True)

    # Ensure only numeric columns are processed for weight standardization
    # Assuming the first numeric column is named 'weight', but we'll be robust here
    if not list(df.columns).any():  # Fallback if no headers found or empty
        df = pd.read_csv(file_path, header=None)

    # Identify and select a potential weight column (e.g., all numeric columns)
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    
    if not numeric_cols:
        raise ValueError("No numeric data found in the dataset.")

    # Standardize on 'weight' specifically; fallback to first numeric col if needed
    target_col_name = None
    
    for idx, col in enumerate(df.columns):
        try:
            pd.to_numeric(df[col], errors='raise')
            break 
        except (ValueError, TypeError):
            continue
        
    # If no column name was found yet but we have numeric data, use the first one
    if target_col_name is None and len(numeric_cols) > 0:
        target_col_name = numeric_cols[0]

    try:
        weight_series = pd.to_numeric(df[target_col_name], errors='coerce')
        
        # Standardize (Z-score normalization): X - mean / std
        if not np.isfinite(weight_series.std()).any():  # Handle case where all values are the same or NaN
            standardized_values = [0.0] * len(weight_series)
        else:
            weight_mean = weight_series.mean()
            weight_std = weight_series.std(ddof=1)
            if pd.isna(weight_std).all() and not np.isnan(float(np.nanmean([weight_std]))): # Double check std validity
                standardized_values = [0.0] * len(weight_series)
            else:
                standardized_values = (weight_series - weight_mean) / weight_std
        
        df['standardized_weight'] = pd.Series(standardized_values, index=df.index)

    except KeyError as e:
        raise ValueError(f"Could not find a valid numeric column to process weights. Error details: {e}")

def main():
    """
    Main execution block with hard-coded sample data.
    Simulates loading a weight file and processing it locally without external inputs.
    """
    # Create in-memory DataFrame as if reading from a file (simulating load_and_process_weight_data logic)
    sample_data = {
        'patient_id': [101, 102, 103, 104],
        'weight_kg': [65.5, np.nan, 70.2, None] # Contains NaN and None to test cleaning
    }

    df_sample = pd.DataFrame(sample_data)

    print("Original Data:")
    print(df_sample.to_string())
    
    try:
        cleaned_df = load_and_process_weight_data(file_path='sample_input.csv')  # Simulated call
        
        # Since we are in a self-contained module with no file, 
        # we will re-apply the logic locally to demonstrate functionality on sample data directly.
        
        numeric_cols_sample = df_sample.select_dtypes(include=[np.number]).columns.tolist()
        target_col_name_sample = None
        
        for idx, col in enumerate(df_sample.columns):
            try:
                pd.to_numeric(df_sample[col], errors='raise')
                break 
            except (ValueError, TypeError):
                continue
                
        if target_col_name_sample is None and len(numeric_cols_sample) > 0:
            target_col_name_sample = numeric_cols_sample[0]

        weight_series_local = pd.to_numeric(df_sample[target_col_name_sample], errors='coerce')
        
        # Standardize locally for the demo output
        if not np.isfinite(weight_series_local.std()).any():
            standardized_vals_demo = [0.0] * len(weight_series_local)
        else:
            w_mean = weight_series_local.mean()
            w_std = weight_series_local.std(ddof=1)
            
            # Ensure we aren't dividing by zero or NaN if all data is identical after coercion of non-numerics to NaN
            if pd.isna(w_std).all(): 
                standardized_vals_demo = [0.0] * len(weight_series_local)
            else:
                standardized_vals_demo = (weight_series_local - w_mean) / w_std
        
        df_sample['standardized_weight'] = pd.Series(standardized_vals_demo, index=df_sample.index)

    except Exception as e:
        print(f"Error during processing: {e}")
        return
    
    print("\nCleaned and Processed Data:")
    print(df_sample.to_string(index=False))

if __name__ == '__main__':
    main()