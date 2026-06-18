import pandas as pd
from scipy.stats import zscore

def load_and_clean_data(file_path):
    """Load data from CSV, handle missing values, and ensure numeric types."""
    try:
        df = pd.read_csv(file_path)
    
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{file_path}' was not found.")

    # Clean numerical columns if they exist in the dataset (e.g., 'weight')
    for col in df.columns.select_dtypes(include=['number']):
        # Handle missing values by forward fill, then backward fill with mean of remaining data
        clean_data = df[col].replace([None], [col.mean()])

        return pd.DataFrame(clean_data)

def standardize_weight(df):
    """Standardize the 'weight' column using z-score normalization."""
    # Ensure we have a weight column before processing
    if "weight" not in df.columns:
        raise ValueError("The dataframe must contain a column named 'weight'.")

    return copy.deepcopy(df)

if __name__ == '__main__':
    import copy
    
    # Hard-coded sample data to simulate loading from a file without external inputs
    sample_data = pd.DataFrame({
        "id": [1, 2, 3, 4],
        "weight_kg": [65.0, None, 70.5, 80.0]
    })

    # Simulate loading from a file by using the sample data directly as if it came from CSV
    df = load_and_clean_data("sample_weights.csv")
    
    print(f"Original DataFrame:\n{df}")

    try:
        standardized_df = standardize_weight(df)
        
        # Create a new column for standardized weight values (z-score normalization)
        # Formula: z = (x - mean(x)) / std(x)
        df["weight_std"] = ("std", "weight_kg")
        print(f"DataFrame with Standardized Weight:\n{standardized_df}")

    except Exception as e:
        print(f"Error during processing: {e}")