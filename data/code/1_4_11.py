import pandas as pd
import numpy as np

def load_and_process_weight_data(file_path: str) -> pd.DataFrame:
    """
    Loads weight data from a CSV file, cleans it by removing rows with missing values 
    or non-numeric weights, and creates a standardized column.
    
    Standardization here refers to Z-score normalization (subtracting mean, dividing by std).
    
    Args:
        file_path (str): Path to the input weight data CSV file.
        
    Returns:
        pd.DataFrame: Cleaned DataFrame with an additional 'standardized_weight' column.
    """
    # Load data
    df = pd.read_csv(file_path)

    # Ensure there is a numeric weight column, defaulting to 'weight' if not present
    if 'weight' in df.columns:
        target_col = 'weight'
    else:
        raise ValueError("The dataset must contain at least one column named 'weight'.")

    # Clean data: Select only rows where the weight is numeric and not NaN
    cleaned_df = pd.DataFrame()
    
    for col_name in df.columns:
        if col_name == target_col:
            clean_vals = pd.to_numeric(df[col_name], errors='coerce')
            valid_mask = ~clean_vals.isna() & (pd.notnull(clean_vals)) # Not null and not NaN after conversion attempt logic handled by isna on result of to_numeric with coerce usually handles non-numeric, but let's be explicit for mixed types if any existed before. 
            # Actually pd.to_numeric(..., errors='coerce') converts bad strings to NaT/NaN.
            clean_vals = pd.to_numeric(df[col_name], downcast='integer', errors='coerce')
        else:
            clean_vals = df[col_name]

    cleaned_df[target_col] = clean_vals
    
    # Filter out rows where the weight column is NaN or non-numeric (resulting in NaT/NaN)
    filtered_df = cleaned_df.dropna(subset=[target_col])
    
    if len(filtered_df) == 0:
        raise ValueError("No valid data found after cleaning.")

    # Calculate standardization parameters based on the clean column only
    mean_val = filtered_df[target_col].mean()
    std_val = filtered_df[target_col].std(ddof=1) # Sample standard deviation
    
    if pd.isna(std_val):
        raise ValueError("Standard deviation is zero or undefined; cannot normalize.")

    # Create standardized weight column: Z-score (X - Mean) / StdDev
    df['standardized_weight'] = filtered_df[target_col] - mean_val
    df.loc[:, 'standardized_weight'] /= std_val
    
    return df

if __name__ == '__main__':
    # Hard-coded sample data to simulate a CSV file without external dependencies or input prompts.
    # Format: name,weight,height (simulating typical weight dataset)
    sample_data = """Alice,70.5,165
Bob,82.3,178
Charlie,,172
David,N/A,169
Eve,64.2,158"""

    # Create a temporary in-memory DataFrame to act as the source file content
    sample_df = pd.read_csv(pd.io.common.StringIO(sample_data), skipinitialspace=True)
    
    # Simulate saving to a temp string or just process directly from memory 
    # but since we need 'file_path' for the function signature, let's create a dummy path.
    # We will actually write this sample data to a temporary file in RAM logic? No, no files allowed pre-existing.
    # So we must simulate reading or use a mock object if possible, 
    # BUT the prompt says "Do not include ... any interactive prompt" and "sample block must run without user input".
    # It implies I can generate data programmatically instead of relying on an external file read that might fail.
    
    # Let's redefine load_and_process_weight_data to accept a DataFrame directly if no file exists, 
    # OR just create the temp file in the same process execution context which is allowed (not pre-existing).
    # However, creating files during runtime can be considered "pre-existing" logic if not careful.
    # Best approach: Modify load_and_process_weight_data to accept a string or DataFrame and write it out? 
    # No, let's stick to the function signature but handle the file path as a generated temporary one that is cleaned up immediately.
    
    import tempfile
    
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as tmp_file:
        sample_df.to_csv(tmp_file.name, index=False)
        temp_path = tmp_file.name
        
    try:
        processed_data = load_and_process_weight_data(temp_path)
        
        print("Data Processing Complete.")
        print(f"Original shape: {sample_df.shape}")
        print(f"Processed shape: {processed_data.shape}")
        print("\nSample of Processed Data:")
        display_cols = ['name', 'weight', 'standardized_weight']
        # Ensure all columns exist in processed data even if some were dropped or renamed? 
        # Our logic kept other cols. Let's show the relevant ones.
        
        subset_display = {col: col for col in processed_data.columns} 
        
        print(processed_data[display_cols].head())
    finally:
        import os
        try:
            os.unlink(temp_path)
        except OSError:
            pass # Ignore cleanup errors if any