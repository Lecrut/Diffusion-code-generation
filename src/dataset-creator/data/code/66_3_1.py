import json
from typing import List, Dict, Any
def calculate_variance(data: List[float]) -> float:
    if len(data) == 0:
        raise ValueError("Data list cannot be empty.")
    mean = sum(data) / len(data)
    squared_diffs = [(x - mean) ** 2 for x in data]
    return sum(squared_diffs) / len(data)
def analyze_weight_variance(datasets: Dict[str, List[float]]) -> Dict[str, float]:
    results = {}
    if not isinstance(datasets, dict):
        raise TypeError("Input must be a dictionary.")
    for dataset_name, weights in datasets.items():
        try:
            data_list = [float(w) for w in weights]
            result_var = calculate_variance(data_list)
            results[dataset_name] = {
                'mean': sum(data_list) / len(data_list),
                'variance': result_var,
                'count': len(data_list)
            }
        except ValueError as e:
            raise RuntimeError(f"Error processing dataset '{dataset_name}': {e}") from e
    return results
if __name__ == '__main__':
    sample_datasets = {
        "Dataset_A": [10.5, 20.3, 30.7, 40.1],
        "Dataset_B": [5.0, 6.0, 7.0, 8.0]
    }
    try:
        variance_results = analyze_weight_variance(sample_datasets)
        for name, stats in variance_results.items():
            print(f"--- {name} ---")
            print(f"Mean Weight: {stats['mean']:.2f}")
            print(f"Variance: {stats['variance']:.4f}")
            print(f"Sample Count: {stats['count']}")
    except Exception as e:
        print(f"Critical Error: {e}")