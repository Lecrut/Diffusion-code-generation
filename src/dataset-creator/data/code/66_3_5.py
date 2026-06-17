import json
from typing import List, Dict, Optional
def calculate_variance(data: List[float]) -> float:
    if not data:
        raise ValueError("Input list cannot be empty.")
    n = len(data)
    mean = sum(data) / n
    squared_diffs = [(x - mean) ** 2 for x in data]
    return sum(squared_diffs) / (n - 1)
def analyze_weight_variance(dataset: Dict[str, List[float]]) -> Optional[Dict]:
    if not dataset or any(not values for values in dataset.values()):
        raise ValueError("Dataset must contain non-empty lists of weights.")
    results = {}
    for name, weights in dataset.items():
        try:
            var = calculate_variance(weights)
            results[name] = {
                "variance": round(var, 6),
                "count": len(weights)
            }
        except Exception as e:
            raise RuntimeError(f"Error processing '{name}': {str(e)}")
    return results
if __name__ == '__main__':
    sample_datasets = {
        "dataset_a": [10.5, 20.3, 19.8, 21.2],
        "dataset_b": [5.0, 6.0, 7.0]
    }
    try:
        variance_report = analyze_weight_variance(sample_datasets)
        print(json.dumps(variance_report, indent=4))
    except Exception as e:
        print(f"Critical error occurred: {e}")