import pandas as pd
import numpy as np

def load_and_process_weight_data():
    """
    Creates a sample DataFrame with weight data, cleans it by handling missing values 
    and outliers using interquartile range (IQR) method if necessary, 
    and generates a standardized column.
    
    Returns:
        pd.DataFrame: Cleaned dataframe with the 'standardized_weight' column added.
    """
    # Create sample data directly without file I/O to satisfy non-interactive requirements
    raw_data = {
        "id": [1, 2, 3, 4, 5],
        "weight_kg": [60.0, np.nan, 75.5, 82.0, None] # Include NaN and string 'None' to test cleaning
    }

    df = pd.DataFrame(raw_data)

    # Data Cleaning Steps:
    
    # Step 1: Convert non-numeric weight values (like the string "None") back to float where possible or fill them later.
    # In this specific sample, None is already NaN in pandas DataFrame creation usually, 
    # but if it were a string like "'None'", we would handle conversion here.
    df["weight_kg"] = pd.to_numeric(df["weight_kg"], errors='coerce')

    # Step 2: Handle missing values by filling with the median (robust against outliers) to avoid dropping data entirely,
    # though for standardization later, we might prefer imputation or removal. Here we fill with Median.
    median_weight = df["weight_kg"].median()
    
    # Fill NaNs with the calculated median
    df["weight_kg"] = df["weight_kg"].fillna(median_weight)

    # Step 3: Identify and remove potential extreme outliers using IQR method 
    # to ensure standardization is not skewed by data points far outside normal range.
    Q1 = df["weight_kg"].quantile(0.25)
    Q3 = df["weight_kg"].quantile(0.75)
    IQR = Q3 - Q1
    
    # Define bounds (typically 1.5 * IQR for boxplot method, using 3 here to be more strict if needed, 
    # but standard is often 1.5 or 2. Let's stick to a reasonable threshold of > 2*IQR)
    lower_bound = Q1 - (2 * IQR)
    upper_bound = Q3 + (2 * IQR)

    # Filter out rows that are significantly outliers based on the calculated bounds
    df_cleaned = df[(df["weight_kg"] >= lower_bound) & (df["weight_kg"] <= upper_bound)].copy()

    # Step 4: Generate standardized weight column.
    # Standardization formula: Z-score = (x - mean) / std
    z_score_mean = df_cleaned["weight_kg"].mean()
    z_score_std = df_cleaned["weight_kg"].std(ddof=0) # Population standard deviation

    if z_score_std == 0:
        standardized_weight_col_name = "standardized_weight"
        df[standardized_weight_col_name] = 0.0
    else:
        df[standardized_weight_col_name] = (df_cleaned["weight_kg"] - z_score_mean) / z_score_std

    return df

if __name__ == '__main__':
    # Execute the pipeline with hard-coded sample values as per requirements
    final_df = load_and_process_weight_data()
    
    print("Processed Data:")
    print(final_df.to_string())