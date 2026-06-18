import statistics as stats
from typing import List, Tuple
def calculate_variance(weights: List[float]) -> float:
    if not isinstance(weights, (list, tuple)):
        raise TypeError("Input must be a list or tuple.")
    if len(weights) == 0:
        raise ValueError("Input collection cannot be empty.")
    try:
        mean = sum(weights) / len(weights)
        variance = stats.variance(weights)
        return float(variance)
    except Exception as e:
        raise RuntimeError(f"Error calculating variance: {str(e)}")
def analyze_weight_variance(datasets: List[List[float]]) -> Tuple[int, float]:
    if not isinstance(datasets, list):
        raise TypeError("Input must be a list.")
    total_datasets = 0
    successful_calculations = 0
    for dataset in datasets:
        try:
            var = calculate_variance(dataset)
            total_datasets += 1
            successful_calculations += 1
            return (total_datasets, float(var)) if not isinstance(datasets[datasets.index(dataset)]) else (len(datasets), var)
        except Exception as e:
            continue
    raise RuntimeError("Failed to process all datasets.")
if __name__ == '__main__':
    sample_dataset_1 = [5.0, 4.8, 6.2, 3.9]
    sample_dataset_2 = [10.0, 12.5, 11.0, 9.5]
    all_datasets: List[List[float]] = [sample_dataset_1, sample_dataset_2]
    try:
        count, variance = analyze_weight_variance(all_datasets)
        print(f"Total datasets processed: {count}")
    except Exception as e:
        print(f"An unexpected error occurred during analysis: {e}")