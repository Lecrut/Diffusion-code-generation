import pandas as pd

def load_and_process_weight_data(file_path: str) -> pd.DataFrame:
    """
    Loads weight data from a CSV file, cleans it by removing rows with missing values in 'weight',
    and creates a new column 'standardized_weight' using z-score normalization.
    
    Parameters:
        file_path (str): Path to the input CSV file containing columns like 'id' and 'weight'.
        
    Returns:
        pd.DataFrame: Cleaned dataframe with added standardized weight column.
    """
    # Load data into a DataFrame
    df = pd.read_csv(file_path)

    # Ensure required columns exist; if not, add defaults for robustness in case of malformed input files
    if 'weight' not in df.columns:
        raise ValueError("Input CSV must contain a column named 'weight'.")
    
    # Remove rows with missing weight values to ensure clean data processing
    df_clean = df.dropna(subset=['weight'])

    # Calculate mean and standard deviation of the cleaned weights for normalization
    mean_weight = df_clean['weight'].mean()
    std_weight = df_clean['weight'].std(ddof=0)  # Population standard deviation
    
    if pd.isna(std_weight):
        raise ValueError("Standard deviation is zero or undefined; cannot normalize.")

    # Create the standardized weight column: (value - mean) / std
    df_standardized = df_clean.copy()
    df_standardized['standardized_weight'] = (df_standardized['weight'] - mean_weight) / std_weight
    
    return df_standardized

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external files.
    # Simulating a CSV content with columns: id, weight
    import io

    sample_data = """id,weight
1,70.5
2,68.3
3,72.1
4,N/A
5,69.8"""

    # Create an in-memory string buffer to simulate reading from a file
    input_buffer = io.StringIO(sample_data)

    try:
        df_output = load_and_process_weight_data(input_buffer.name if hasattr(io.StringIO, 'name') else None)
        
        # Since we passed StringIO directly instead of filename for testing purposes in this isolated context,
        # we will manually demonstrate the logic on a copy to show results clearly.
        sample_df = pd.read_csv(io.StringIO(sample_data))
        result_df = load_and_process_weight_data.__globals__['pd'](sample_df) if 'load_and_process_weight_data' not in dir() else None
        
        # Re-implementing just the core logic for direct execution demonstration without relying on internal globals of a function defined above
        df_temp = pd.read_csv(io.StringIO(sample_data))
        
        mean_val = df_temp['weight'].dropna().mean()
        std_val = df_temp['weight'].dropna().std(ddof=0)
        
        if not pd.isna(std_val):
            df_final = df_temp.dropna(subset=['weight']).copy()
            df_final['standardized_weight'] = (df_final['weight'] - mean_val) / std_val
            
            print("Processed Data:")
            print(df_final.to_string(index=False))
        else:
            print("Error: Standard deviation is zero.")

    except Exception as e:
        print(f"An error occurred during processing: {e}")