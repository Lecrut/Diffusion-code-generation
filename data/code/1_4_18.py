import pandas as pd

def load_and_process_weight_data(file_path: str) -> pd.DataFrame:
    """
    Loads weight data from a CSV file, cleans it by converting necessary columns to numeric types 
    and handling missing values, then generates a standardized weight column.
    
    Args:
        file_path (str): Path to the input CSV file containing raw weight data.
        
    Returns:
        pd.DataFrame: A cleaned DataFrame with an additional 'standardized_weight' column.
    """
    # Load the dataset from the specified path
    df = pd.read_csv(file_path)

    # Identify and convert relevant columns (assuming generic structure based on common datasets)
    numeric_columns = ['weight', 'height']  # Adjust based on actual file content if needed
    
    for col in numeric_columns:
        try:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        except Exception:
            pass

    # Handle missing values by filling with the column mean (or median) to ensure data integrity
    numerical_cols_to_fill = [col for col in numeric_columns if col not in ['standardized_weight']]
    
    df[numerical_cols_to_fill] = df[numerical_cols_to_fill].fillna(df[numerical_cols_to_fill].mean())

    # Generate standardized weight values using Z-score normalization: (x - mean) / std_dev
    original_weights = df['weight']
    mean_weight = original_weights.mean()
    std_weight = original_weights.std()

    if std_weight != 0:
        df['standardized_weight'] = ((original_weights - mean_weight) / std_weight).round(4)
    else:
        # If standard deviation is zero, all values are the same; set standardized weight to 0
        df['standardized_weight'] = 0.0

    return df

if __name__ == '__main__':
    # Hard-coded sample data simulating a CSV file structure without external dependencies
    
    # Sample raw data dictionary mimicking columns: 'id', 'weight' (numeric), 'height' (numeric)
    sample_data = {
        "id": [1, 2, 3, 4, 5],
        "name": ["Alice", "Bob", "Charlie", "David", "Eve"],
        "raw_weight_kg": [60.5, None, 75.2, 80.0, 90.1], # Using a custom column name for variety in cleaning logic
    }

    sample_df = pd.DataFrame(sample_data)
    
    # Rename 'raw_weight_kg' to 'weight' before processing to match function expectations or adapt the function
    # Here we directly pass the dataframe and assume the input file has columns that can be mapped.
    # To strictly adhere to "no files", we will create a temporary DataFrame structure representing 
    # what would come from a file, but since read_csv requires a path string, we simulate by writing logic 
    # that handles the specific column names present in our sample data directly.

    # Re-implementing load_and_process_weight_data to accept a pre-loaded dataframe for this self-contained run
    def process_local_df(df: pd.DataFrame) -> pd.DataFrame:
        """Process local DataFrame instead of reading from file."""
        
        # Ensure 'weight' column exists and is numeric, handling potential different naming if needed.
        # In the sample data above we have 'raw_weight_kg'. We will treat this as our weight source 
        # or assume a standard 'weight' column for consistency with typical tasks. 
        # Let's rename 'raw_weight_kg' to 'weight' and proceed.
        
        if 'weight' not in df.columns:
            # Fallback mapping logic for the sample data provided above
            col_map = {'id': 'id', 'name': 'name', 'raw_weight_kg': 'weight'}
            
            new_df = pd.DataFrame(columns=df.columns)
            rename_dict = {k: v for k, v in col_map.items() if k in df.columns}
            df.rename(columns=rename_dict, inplace=True)

        # Convert weight to numeric handling errors (e.g. non-numeric strings or NaNs initially present)
        try:
            df['weight'] = pd.to_numeric(df['weight'], errors='coerce')
        except Exception:
            pass
            
        # Handle missing values with mean of the 'weight' column
        weight_mean = df['weight'].mean()
        
        if not pd.isna(weight_mean):
            df['weight'] = df['weight'].fillna(weight_mean)

        # Calculate standard deviation for normalization
        std_dev = df['weight'].std()
        
        if std_dev != 0:
            df['standardized_weight'] = ((df['weight'] - weight_mean) / std_dev).round(4)
        else:
            df['standardized_weight'] = 0.0
            
        return df

    # Execute processing on the sample data directly without file I/O simulation overhead 
    final_df = process_local_df(sample_df.copy())

    print("Original Data:")
    print(final_df[['id', 'name', 'weight']].to_string(index=False))
    
    print("\nProcessed Data with Standardized Weight:")
    print(final_df.to_string(index=False))