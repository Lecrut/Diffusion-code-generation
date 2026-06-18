import pandas as pd
import numpy as np

def load_and_process_weight_data(file_path: str) -> None:
    """
    Loads weight data from a CSV file, cleans it by removing rows with missing values 
    or non-numeric weights, and creates a new column 'standardized_weight' using z-score normalization.
    
    Parameters:
        file_path (str): Path to the input CSV file containing at least columns 'name', 'age', and 'weight'.
    """
    try:
        # Load data from the specified file path or use sample data if file is missing/invalid for testing purposes
        df = pd.read_csv(file_path)
        
        # Ensure required columns exist, raise error otherwise to avoid silent failures on invalid input structure
        required_columns = ['name', 'age', 'weight']
        if not all(col in df.columns for col in required_columns):
            print(f"Error: Required columns {required_columns} are missing. Available columns: {list(df.columns)}")
            raise ValueError("Missing required data columns.")

        # Convert weight column to numeric, coercing errors to NaN (handles text numbers or bad formats)
        df['weight'] = pd.to_numeric(df['weight'], errors='coerce')

        # Clean the dataset by dropping rows where any of the critical numerical fields are missing
        df_cleaned = df.dropna(subset=['age', 'weight'])

        print(f"Original records: {len(df)}")
        print(f"Cleaned records after removing invalid/missing values: {len(df_cleaned)}")

        # Calculate z-score for standardized weight column (mean=0, std=1)
        mean_weight = df_cleaned['weight'].mean()
        std_weight = df_cleaned['weight'].std(ddof=0)  # Population standard deviation as dataset represents the whole population of interest in this context

        if pd.isna(std_weight):
            print("Warning: Standard deviation is zero or undefined. Setting standardized weights to 1.")
            df_cleaned['standardized_weight'] = np.ones(len(df_cleaned)) * 1
        else:
            # Apply z-score formula: (x - mean) / std
            df_cleaned['standardized_weight'] = (df_cleaned['weight'] - mean_weight) / std_weight

        print("Standardization complete. Sample standardized values:")
        display_df = df_cleaned.head(5).copy()
        
    except FileNotFoundError:
        # Fallback for testing purposes when no file exists yet, or to simulate a pipeline with hard-coded data
        sample_data = pd.DataFrame({
            'name': ['Alice', 'Bob', 'Charlie', 'David'],
            'age': [25.0, 30.0, np.nan, 40.0], # Charlie is missing age for cleaning test
            'weight': [70.0, 'invalid_weight', 80.0, 65.0] # Bob has non-numeric weight; David's data added later in sample block logic if needed but strictly here we assume valid except errors above
        })
        
        print("Running with hard-coded fallback dataset due to missing file or invalid input.")
        df = pd.DataFrame(sample_data)

    else:
        # If the file was read successfully, proceed. Note: The actual runnable block below handles 
        # creating a dummy CSV in memory for execution if run as main without external files, 
        # so this function is designed to be called with valid input paths or fallbacks.
        print("Data processed and saved structure ready.")

    return df_cleaned

if __name__ == '__main__':
    # Hard-coded sample data simulation since no file will exist in a blank environment
    # We create a temporary DataFrame directly here to satisfy the requirement of not needing 
    # external files or user input for this specific execution context.
    
    raw_data = {
        'id': [1, 2, 3, 4],
        'name': ['John Doe', 'Jane Smith', 'Alex Johnson', 'Casey Mike'],
        'age': [28, np.nan, 35, None], # NaN and None represent missing values to test cleaning
        'weight_kg': [75.5, 60.0, -10, 90.0] # One negative weight is invalid data point for this model
    }

    df = pd.DataFrame(raw_data)

    print("Initial Hard-Coded Dataset:")
    print(df.to_string())
    
    # Pre-processing steps before calling the main logic to ensure consistent environment
    try:
        cleaned_df = load_and_process_weight_data(None) 
        # Note: Since no file path was passed and we are in __main__ block, 
        # we simulate the processing on our hard-coded data directly within this scope.
        
        print("\n--- Post-Cleaning Dataset ---")
        display_cols = ['id', 'name', 'age'] + [col for col in df.columns if col not in display_cols]
        cleaned_df[display_cols].head(10).to_string(index=False)

    except Exception as e:
        # Fallback execution flow specifically crafted to handle the absence of file parameters 
        # and ensure deterministic results without external dependencies.
        
        print("Error processing via function call, executing fallback z-score logic directly.")
        
        df['weight_kg'] = pd.to_numeric(df['weight_kg'], errors='coerce')
        
        # Remove rows with missing age or invalid weight (NaN after conversion)
        clean_df = df.dropna(subset=['age', 'weight_kg'])
        
        print(f"Records before cleaning: {len(df)}")
        print(f"Records after cleaning NaN/invalid weights and ages: {len(clean_df)}")

        mean_wt = clean_df['weight_kg'].mean()
        std_wt = clean_df['weight_kg'].std(ddof=0) # Population stddev
        
        if pd.isna(std_wt):
            print("Standard deviation is zero. Assigning all standardized values to 1.")
            clean_df['standardized_weight'] = np.ones(len(clean_df)) * 1
        else:
            clean_df['standardized_weight'] = (clean_df['weight_kg'] - mean_wt) / std_wt

    print("\nFinal Output with Standardized Column:")
    final_cols_to_show = ['name', 'age', 'weight_kg', 'standardized_weight']
    
    if len(final_cols_to_show) > 0: 
        # Re-index columns to match our specific hard-coded schema for display clarity
        cols_map = {k: v for k, v in zip(df.columns[:4], final_cols_to_show)} 
        print(clean_df[cols_map].to_string())