import math
def check_threshold(value: float, threshold: float) -> bool:
    return value >= threshold
def process_data(data_list: list[float]) -> dict[str, any]:
    results = {
        "count": len(data_list),
        "max_value": max(data_list),
        "min_value": min(data_list),
        "sum_total": sum(data_list)
    }
    if check_threshold(results["max_value"], 100):
        results["flagged"] = True
    else:
        results["flagged"] = False
    return results
if __name__ == '__main__':
    sample_data = [45.2, 98.7, 33.1, 150.0, 67.8]
    output = process_data(sample_data)
    print(f"Data processed: {output}")