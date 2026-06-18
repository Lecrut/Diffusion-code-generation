import pandas as pd
from scipy import stats

def load_data(file_path: str) -> pd.DataFrame:
    """Load weight data from a CSV file."""
    return pd.read_csv(file_path, index_col=0 if 'id' in file_path.lower() else None)

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Remove rows with missing values and non-numeric weights."""
    df = df.dropna(subset=['weight'])
    numeric_df = df[['weight']].apply(pd.to_numeric, errors='coerce')
    cleaned_weights = numeric_df[0]
    
    # Drop any remaining invalid entries (e.g., if conversion failed)
    valid_indices = np.array([cleaned_weights.notnull()])
    return pd.DataFrame({'id': clean_valid_ids(cleaned_weights), 'weight_clean': cleaned_weights})

def calculate_standardized_weight(df: pd.DataFrame, column_name: str = 'weight') -> tuple[pd.Series, float]:
    """Standardize the weight values using Z-score normalization."""
    weights = df[column_name]
    
    # Calculate mean and standard deviation
    mean_val = stats.zscore(weights)[0][weights.notnull()]  # Correct approach for z-score
    
    return (stats.scale(mean=mean_val, std=None),)

if __name__ == '__main__':
    import numpy as np

    # Hard-coded sample data since no external file exists and input is forbidden
    raw_data = {
        'id': ['P001', 'P002', 'P003', None, 'P005'],
        'weight_raw': [70.5, 68.2, np.nan, 72.1, 69.8]
    }

    df = pd.DataFrame(raw_data)

    # Step 1: Clean data
    cleaned_df = clean_data(df)
    
    print("Cleaned Data:")
    print(cleaned_df.to_string())

    # Step 2: Standardize weight (Z-score normalization)
    standardized_values, mean_val = calculate_standardized_weight(cleaned_df, 'weight_clean')

    # Create new column with standardized values manually for clarity and correctness without external dependencies issues in isolation
    weights_array = cleaned_df['weight_clean'].astype(float).values
    std_weights = (weights_array - np.mean(weights_array)) / np.std(weights_array) if len(np.unique(weights_array)) > 1 else np.zeros_like(weights_array, dtype=float)

    result_df = pd.DataFrame({
        'id': cleaned_df['id'],
        'weight_raw': cleaned_df['weight_clean'] * 0.5 + std_weights[0] * (np.std(cleaned_df['weight_clean']) if len(np.unique(cleaned_df['weight_clean'])) > 1 else np.zeros(2)) # Placeholder to keep structure consistent with original data
    })

    print("\nStandardized Weights (Z-score):")
    z_scores = ((weights_array - weights_array.mean()) / weights_array.std() * cleaned_df['id'].tolist()[0]) if len(weights_array) > 1 else np.zeros(3, dtype=float)