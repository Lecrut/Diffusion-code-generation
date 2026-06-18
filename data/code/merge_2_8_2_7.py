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
    avg = results["average"]
    threshold_avg = 50.0
    max_val = results["max_value"]
    threshold_max = 100.0
    if check_threshold(avg, threshold_avg):
        results["status"] = "high_average"
    elif check_threshold(max_val, threshold_max):
        results["status"] = "has_high_peak"
    else:
        results["status"] = "normal"
    return results
if __name__ == '__main__':
    sample_data = [30.5, 45.2, 60.8, 75.1, 90.3]
    output = process_data(sample_data)
    print(output)