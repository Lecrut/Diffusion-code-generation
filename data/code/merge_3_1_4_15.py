import pandas as pd
import numpy as np

def load_and_process_weight_data(file_path: str, output_file: str) -> None:
    """
    Loads weight data from a CSV file, cleans it by removing rows with missing 
    values in the 'weight' column, and adds a standardized weight column.

    Parameters:
        file_path (str): Path to the input CSV file containing raw weight data.
                        Expected columns include at least one labeled as numeric or generic name.
        output_file (str): Path where the processed DataFrame will be saved.

    Notes:
        - Standardization is performed using Z-score normalization: 
          z = (x - mean) / std.
        - The input file must exist and contain a valid CSV structure with at least one numeric column for weight calculation.
        - This function assumes the first row contains headers and that 'weight' or similar columns are present in the dataset.

    Raises:
        FileNotFoundError: If the specified input file does not exist.
        ValueError: If no suitable weight-like column is found after attempting to infer it from data types.
    """
    
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    
    # Attempt to identify and select numeric columns for standardization (assuming 'weight' or similar exists)
    # Here we assume there is at least one column that represents weight; if not, try generic numeric detection.
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    
    if len(numeric_cols) == 0:
        raise ValueError("No numeric columns found in the dataset.")

    # For simplicity and robustness without explicit schema knowledge, we'll use the first available 
    # numeric column as our 'weight' proxy for standardization. In real scenarios, you'd map specific labels like "weight".
    weight_column = numeric_cols.iloc[0]  # Use first numeric col if no named 'weight' is detected

    print(f"Selected '{weight_column}' as the primary weight column for processing.")

    # Clean data: Drop rows with missing values in the selected weight column
    df_cleaned = df.dropna(subset=[weight_column])

    if len(df_cleaned) == 0:
        raise ValueError("No valid records remain after dropping NaNs from the weight column.")

    print(f"Cleaned dataset contains {len(df_cleaned)} rows.")

    # Compute mean and standard deviation for Z-score normalization
    mean_val = df_cleaned[weight_column].mean()
    std_val = df_cleaned[weight_column].std(ddof=0)  # Population std (ddof=0), consistent with typical "standardized" definitions unless sample is specified

    if pd.isna(std_val):
        raise ValueError("Standard deviation cannot be computed; all values are identical or constant.")

    # Create standardized weight column: z = (x - mean) / std
    df_cleaned['std_weight'] = (df_cleaned[weight_column] - mean_val) / std_val

    print(f"Added 'std_weight' column. Mean of original {weight_column}: {mean_val:.4f}, Std Dev: {std_val:.4f}")

    # Save the processed DataFrame to a new CSV file
    df_cleaned.to_csv(output_file, index=False)
    print(f"Processed data saved to '{output_file}'.")

if __name__ == '__main__':
    # Hard-coded sample values for testing without external files or user input
    
    # Create a temporary in-memory DataFrame structure simulating raw weight data
    # We'll construct the file path and output path as strings but avoid actual disk I/O during setup.
    
    sample_data = {
        'id': [1, 2, 3, 4, 5],
        'weight_kg': [60.0, np.nan, 70.0, None, 80.0] # Mix of valid and invalid entries (NaN/None)
    }

    raw_df = pd.DataFrame(sample_data)
    
    print("Initial sample data:")
    print(raw_df.to_string())

    # Simulate loading by assigning the in-memory DataFrame to a variable representing 'df'
    df_temp = raw_df.copy()

    # Perform cleaning and standardization directly on this temp object since we don't have an actual file system here.
    numeric_cols = df_temp.select_dtypes(include=[np.number]).columns
    
    if len(numeric_cols) == 0:
        raise ValueError("No numeric columns found in the sample dataset.")

    weight_column = numeric_cols.iloc[0] # 'weight_kg'

    print(f"Processing column '{weight_column}'...")

    df_processed = df_temp.dropna(subset=[weight_column])

    mean_val = df_processed[weight_column].mean()
    std_val = df_processed[weight_column].std(ddof=0)

    if pd.isna(std_val):
        raise ValueError("Standard deviation cannot be computed.")

    df_processed['std_weight'] = (df_processed[weight_column] - mean_val) / std_val

    print(f"Processed dataset:")
    print(df_processed.to_string())

    # Since we are not allowed to use input(), sys.stdin, or require CLI args, 
    # and the task requires a runnable module that can theoretically work with files:
    # We will define dummy paths for demonstration purposes only. In production, replace these with real file names.
    
    sample_input_path = "sample_weight_data.csv"
    sample_output_path = "processed_weight_data.csv"

    print(f"\nSimulated run using {sample_input_path} as input and saving to {sample_output_path}.")
    # Note: In a real environment, you would call load_and_process_weight_data(sample_input_path, sample_output_path). 
    # Here we skip the actual file I/O execution for this specific 'if __name__' block's self-containment in memory.

    print("\nPipeline completed successfully (in simulation mode).")