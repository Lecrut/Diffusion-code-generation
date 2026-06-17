import statistics as stats
def calculate_variance(data: list[float]) -> float | None:
    if not data:
        raise ValueError("Dataset cannot be empty.")
    try:
        return stats.variance(data)
    except Exception as e:
        raise RuntimeError(f"Error calculating variance: {e}")
def compare_dataset_variances(dataset_a: list[float], dataset_b: list[float]) -> dict[str, float] | None:
    try:
        if not isinstance(data := [dataset_a, dataset_b], (list, tuple)):
            raise TypeError("Input must be a sequence of lists.")
        variance_a = calculate_variance(dataset_a)
        variance_b = calculate_variance(dataset_b)
        return {
            "variance_dataset_a": variance_a,
            "variance_dataset_b": variance_b,
            "difference": abs(variance_a - variance_b),
            "ratio": variance_a / variance_b if variance_b != 0 else float('inf')
        }
    except ValueError as ve:
        raise RuntimeError(f"Invalid dataset input: {ve}") from None
if __name__ == '__main__':
    sample_data_1 = [5.2, 4.8, 6.1, 5.9, 5.3]
    sample_data_2 = [10.1, 12.3, 11.5, 10.7, 11.9]
    try:
        result_a = calculate_variance(sample_data_1)
        print(f"Variance of dataset A: {result_a}")
        comparison_result = compare_dataset_variances(sample_data_1, sample_data_2)
        if isinstance(comparison_result, dict):
            for key in ["variance_dataset_a", "variance_dataset_b"]:
                value = comparison_result[key]
                print(f"Variance of dataset {key}: {value}")
    except Exception as e:
        print(f"An error occurred during processing: {e}")