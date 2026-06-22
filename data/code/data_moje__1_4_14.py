import pandas as pd
import numpy as np

def process_weight_data():
    sample_data = {
        "name": ["Alice", "Bob", "Charlie", "Diana"],
        "weight": [55.0, 70.5, "invalid", 60.2]
    }
    df = pd.DataFrame(sample_data)

    df["weight"] = pd.to_numeric(df["weight"], errors="coerce")
    df = df.dropna(subset=["weight"])

    mean_weight = df["weight"].mean()
    std_weight = df["weight"].std()
    df["standardized_weight"] = (df["weight"] - mean_weight) / std_weight

    return df

if __name__ == "__main__":
    result = process_weight_data()
    print(result)