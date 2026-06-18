import pandas as pd
import numpy as np

def load_and_process_weight_data(file_path):
    """
    Loads weight data from a CSV file, cleans it by removing non-numeric rows 
    and handling missing values, then generates standardized weight columns.
    
    Parameters:
        file_path (str): Path to the input CSV file containing 'weight' column(s).
        
    Returns:
        pd.DataFrame: Cleaned DataFrame with standardized weights added as new columns.
    """
    # Load data assuming at least one row and a 'Weight' or similar numeric column exists
    df = pd.read_csv(file_path)

    if "Weight" not in df.columns and any("weight".lower() in col.lower() for col in df.columns):
        weight_col_name = [col for col in df.columns if "weight".lower() in col.lower()][0]
    else:
        raise ValueError("No column containing 'weight' found.")

    # Ensure the target column exists and is numeric, converting to float where needed
    original_weight_column = weight_col_name
    df[original_weight_column] = pd.to_numeric(df[original_weight_column], errors="coerce")

    # Drop rows with missing values in the weight column
    df = df.dropna(subset=[original_weight_column])

    if len(df) == 0:
        raise ValueError("No valid data remaining after cleaning.")

    # Standardize by subtracting mean and dividing by standard deviation (Z-score normalization)
    weights = df[original_weight_column]
    mean_val = weights.mean()
    std_val = weights.std(ddof=1) if len(weights) > 1 else 0.0

    standardized_weights = []
    for val in weights:
        try:
            z_score = (val - mean_val) / std_val if std_val != 0 else 0
            standardized_weights.append(round(z_score, 4))
        except Exception:
            standardized_weights.append(None)

    df["Standardized_Weight"] = standardized_weights

    return df

if __name__ == '__main__':
    # Hard-coded sample data to simulate input file without external dependencies or user prompts.
    sample_data = {
        "ID": [1, 2, 3, 4, 5],
        "Weight_kg": ["60.5", None, "75.2", "", "80.0"],
        "Height_cm": [170, 165, 172, 168, 175]
    }

    # Create a temporary in-memory DataFrame to simulate loading from file
    df = pd.DataFrame(sample_data)

    try:
        cleaned_df = load_and_process_weight_data(file_path="in_memory_sample.csv")
        
        print("Data Processing Complete.")
        print("\nOriginal Data:")
        print(df.to_string())
        print("\nCleaned and Standardized Data:")
        print(cleaned_df.to_string(index=False))

    except Exception as e:
        # Graceful error handling for simulation without actual file access
        if "No valid data" in str(e) or "weight" in str(e).lower():
            print(f"Error during processing (expected with mock): {e}")
        else:
            raise