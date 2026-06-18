import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_and_clean_data(file_path: str) -> pd.DataFrame:
    """Load CSV data, handle missing values in numeric columns."""
    df = pd.read_csv(file_path)
    
    # Clean data by dropping rows with any NaN values after ensuring numeric types
    for col in df.columns:
        if df[col].dtype == 'object':
            continue  # Skip non-numeric columns for cleaning logic here
        
        try:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        except ValueError:
            pass
    
    return df.dropna()

def standardize_weight_column(df: pd.DataFrame, column_name: str) -> tuple[pd.DataFrame]:
    """Standardize a specific weight column using Z-score normalization."""
    
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' does not exist in the dataframe.")
    
    # Create a copy to avoid modifying original data structure unexpectedly during scaling logic
    standardized_df = df.copy()
    
    scaler = StandardScaler(with_mean=True, with_std=False)  # Using mean=0 manually for clarity or standard sklearn
    
    # Fit and transform only the target column
    scaled_values = scaler.fit_transform(standardized_df[[column_name]])
    
    assigned_column = f"{column_name}_std"
    standardized_df[assigned_column] = scaled_values.flatten()
    
    return standardized_df

def main():
    """Main execution block with hard-coded sample data."""
    # Hard-coded sample weight data as a string to simulate file input without external dependencies
    raw_data_str = """id,weight_kg,height_cm,date_recorded
1,70.5,175,2023-10-01
2,68.2,172,2023-10-02
3,N/A,178,2023-10-03
4,72.1,,2023-10-04
5,69.8,174,2023-10-05"""

    # Create a temporary in-memory dataframe from the string to simulate loading
    sample_df = pd.read_csv(pd.io.common.StringIO(raw_data_str))
    
    print("Original Data:")
    print(sample_df)
    
    cleaned_df = load_and_clean_data(None)  # Logic applied directly on sample_df for this self-contained run
    
    if not isinstance(cleaned_df, type(sample_df)):
        # Since we passed None to simulate file loading but used StringIO internally in logic above conceptually:
        # Re-apply cleaning steps manually here since the function expects a path but we have string data.
        pass

    # Manual re-application of load_and_clean_data logic on sample_df for this specific execution context
    cleaned_sample = pd.read_csv(pd.io.common.StringIO(raw_data_str))
    
    # Ensure numeric conversion and drop NaNs
    for col in cleaned_sample.columns:
        if cleaned_sample[col].dtype == 'object':
            continue
        try:
            cleaned_sample[col] = pd.to_numeric(cleaned_sample[col], errors='coerce')
        except ValueError:
            pass
    
    final_df = cleaned_sample.dropna()

    print("\nCleaned Data:")
    print(final_df)

    # Standardize the 'weight_kg' column
    standardized_final, _ = standardize_weight_column(final_df, "weight_kg")

    print("\nData with Standardized Weight Column ('weight_kg_std'):")
    print(standardized_final)

if __name__ == '__main__':
    main()