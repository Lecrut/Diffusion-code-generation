import statistics as stats
from typing import List, Tuple
def calculate_variance(weights: List[float]) -> float:
    if len(weights) == 0:
        raise ValueError("The weight list cannot be empty.")
    mean = sum(weights) / len(weights)
    squared_diffs = [(x - mean) ** 2 for x in weights]
    return stats.variance(squared_diffs, ddof=1)
def compare_dataset_variance(dataset_a: List[float], dataset_b: List[float]) -> Tuple[bool, float]:
    try:
        var_a = calculate_variance(dataset_a)
        var_b = calculate_variance(dataset_b)
        if not isinstance(var_a, (int, float)) or not isinstance(var_b, (int, float)):
            raise TypeError("Variance calculation failed.")
        return var_a > var_b, abs(var_a - var_b)
    except Exception as e:
        print(f"Error during variance comparison: {e}")
        return False, 0.0
if __name__ == '__main__':
    dataset_x = [10.5, 12.3, 11.8, 9.7, 13.2]
    dataset_y = [5.0, 6.0, 4.5, 5.5, 6.5]
    try:
        is_x_higher, diff_value = compare_dataset_variance(dataset_x, dataset_y)
        print(f"Difference in variance values: {diff_value}")
        if is_x_higher:
            print("Dataset X has higher weight variability.")
        else:
            print("Dataset Y has higher weight variability or equal.")
    except ValueError as ve:
        print(f"Value Error encountered: {ve}")
    except TypeError as te:
        print(f"Type Error encountered: {te}")