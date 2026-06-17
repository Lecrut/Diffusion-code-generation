import statistics as stats
def calculate_variance(data: list[float]) -> float | None:
    if not data:
        raise ValueError("Dataset cannot be empty.")
    try:
        return stats.variance(data)
    except Exception as e:
        raise RuntimeError(f"Error calculating variance: {e}")
def compare_dataset_variances(dataset_a: list[float], dataset_b: list[float]) -> dict[str, float]:
    try:
        return {
            "dataset_a_variance": calculate_variance(dataset_a),
            "dataset_b_variance": calculate_variance(dataset_b)
        }
    except Exception as e:
        raise RuntimeError(f"Error comparing dataset variances: {e}")
if __name__ == '__main__':
    sample_data_1 = [23.5, 40.7, 68.9, 12.3]
    sample_data_2 = [10.1, 20.2, 30.3, 40.4]
    result_a = calculate_variance(sample_data_1)
    print(f"Variance of dataset A: {result_a}")
    comparison_result = compare_dataset_variances(sample_data_1, sample_data_2)
    print("Comparison Result:", comparison_result)