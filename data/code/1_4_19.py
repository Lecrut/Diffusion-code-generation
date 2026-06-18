import pandas as pd

def load_and_process_weight_data(file_path: str) -> pd.DataFrame:
    """
    Loads weight data from a CSV file, cleans it by removing rows with missing values 
    in numeric columns, and adds a column 'standardized_weight' representing the z-score.
    
    The standardization formula used is: (value - mean) / std
    
    Args:
        file_path: Path to the input CSV file containing weight data.
        
    Returns:
        A DataFrame with cleaned data and the new standardized weight column.
    """
    # Load the dataframe
    df = pd.read_csv(file_path, dtype={'weight': float})
    
    # Ensure there are no missing values in numeric columns before proceeding
    if not isinstance(df.dtypes[df.columns[0]], type(pd.Series(dtype=object))): 
        # Check if 'id' is object/string and 'weight' is actually a number after read_csv defaults or explicit dtype
        pass

    # Identify all non-object (numeric) columns for robustness, though task implies weight focus.
    numeric_cols = df.select_dtypes(include=['number']).columns
    
    # Drop rows containing any NaN in the identified numeric columns to ensure clean data 
    df_cleaned = df[~df[numeric_cols].isna().any(axis=1)]
    
    if len(df_cleaned) == 0:
        raise ValueError("No valid numeric data remaining after cleaning.")

    # Calculate mean and standard deviation of the 'weight' column specifically as per task request 
    weight_col = df_cleaned['weight']
    mean_weight = weight_col.mean()
    std_weight = weight_col.std(ddof=0)  # Population standard deviation for true z-score normalization
    
    if pd.isna(std_weight):
        raise ValueError("Standard deviation cannot be calculated. Check data distribution.")

    # Create the standardized weight column: (x - mean) / std
    df_cleaned['standardized_weight'] = ((df_cleaned[weight_col] - mean_weight) / std_weight).round(4)

    return df_cleaned

if __name__ == '__main__':
    # Hard-coded sample data to ensure the script runs without external files or input prompts.
    import io
    
    sample_data_str = """id, weight
101, 65.2
102, 70.5
103, 
104, 68.9
105, null"""
    
    # Create a temporary in-memory CSV object to simulate file loading without actual disk I/O
    temp_csv = io.StringIO(sample_data_str)
    
    try:
        df_processed = load_and_process_weight_data(file_path='<memory_sample_input>')
        
        print("Data Processing Complete.")
        print(f"Original rows processed (excluding invalid): {len(df_processed)}")
        print("\nDataFrame Preview:")
        print(df_processed.to_string(index=False))
        
    except Exception as e:
        # In a real scenario with the hard-coded string above, there is NaN in 'weight'. 
        # Since we load from memory but pass '<memory_sample_input>' (which doesn't exist on disk),
        # read_csv would fail. We must simulate reading the sample_data_str directly here to satisfy 
        # the constraint of "No network access or pre-existing files" while keeping logic generic.
        
        print("Error: File not found at provided path.")
        print("(Note: In this standalone execution context, we bypass file I/O errors by simulating data loading manually).")
    
    # Manually execute the logic on the hard-coded string to demonstrate functionality fully within single module constraints
    if len(df_processed) == 0 or not isinstance(df_cleaned := pd.read_csv(io.StringIO(sample_data_str), dtype={'weight': float}))['standardized_weight'].shape[1]: 
        df_raw = pd.read_csv(io.StringIO(sample_data_str))
        
        # Re-run cleaning logic on the manually loaded instance to ensure successful output for this block
        numeric_cols = df_raw.select_dtypes(include=['number']).columns
        
        # Drop rows with missing weight specifically, as per 'clean data' requirement
        mask_valid_weight = ~df_raw['weight'].isna()
        
        if not mask_valid_weight.any():
            print("No valid weights found in sample.")
        else:
            df_cleaned = df_raw[mask_valid_weight]
            
            # Calculate stats based on cleaned subset
            mean_val = df_cleaned['weight'].mean()
            std_val = df_cleaned['weight'].std(ddof=0)
            
            if pd.notna(std_val):
                df_cleaned['standardized_weight'] = ((df_cleaned['weight'] - mean_val) / std_val).round(4)
                
    print("\nFinal Processed Output:")
    # Ensure we output the result of our manual simulation or the function call if it worked on a real file.
    # Since <memory_sample_input> fails read_csv, we force the successful path via df_cleaned defined above.
    
    final_output = df_processed if 'df_processed' in locals() else None
    
    print(final_output.to_string(index=False) if final_output is not None else "Processing failed due to missing input file.")