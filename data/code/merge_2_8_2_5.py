import math
def check_threshold(value: float, threshold: float) -> bool:
    return value >= threshold
def process_data(data_list: list[float]) -> dict[str, any]:
    results = {
        "count": len(data_list),
        "max_value": max(data_list) if data_list else None,
        "min_value": min(data_list) if data_list else None,
        "average": sum(data_list) / len(data_list) if data_list else 0.0,
    }
    threshold = results["average"] * 1.5
    has_high_values = any(v > threshold for v in data_list)
    if has_high_values:
        high_value_indices = [i for i, val in enumerate(data_list) if val > threshold]
        results["high_value_count"] = len(high_value_indices)
        results["flagged"] = True
    else:
        results["flagged"] = False
    return results
def calculate_statistics(values: list[float]) -> tuple[float, float]:
    mean_val = sum(values) / len(values) if values else 0.0
    variance = sum((x - mean_val) ** 2 for x in values) / len(values) if values else 0.0
    return mean_val, math.sqrt(variance)
if __name__ == '__main__':
    sample_data = [10.5, 23.4, 89.1, 12.3, 67.8]
    stats_result = process_data(sample_data)
    mean_val, std_dev = calculate_statistics(sample_data)
    print(f"Data processed: {stats_result}")
    print(f"Mean value: {mean_val:.4f}, Standard deviation: {std_dev:.4f}")