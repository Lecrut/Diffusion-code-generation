import math
def check_threshold(value: float, threshold: float) -> bool:
    return value >= threshold
def process_data(data_list: list[float]) -> dict[str, any]:
    results = {
        "count": len(data_list),
        "max_value": max(data_list) if data_list else None,
        "min_value": min(data_list) if data_list else None,
        "mean": sum(data_list) / len(data_list) if data_list else 0.0,
    }
    threshold = results["mean"] * 1.5
    high_values = [x for x in data_list if check_threshold(x, threshold)]
    if high_values:
        results["high_value_count"] = len(high_values)
        results["max_high"] = max(high_values)
    else:
        results["high_value_count"] = 0
        results["max_high"] = None
    return results
if __name__ == '__main__':
    sample_data = [1.2, 3.5, 7.8, 9.1, 4.3]
    output = process_data(sample_data)
    print(output)