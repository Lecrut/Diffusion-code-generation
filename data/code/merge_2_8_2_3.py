import math
def check_threshold(value: float, min_val: float = 0) -> bool:
    return value >= min_val
def process_data(data_list: list[float]) -> dict[str, any]:
    results = {}
    if len(data_list) > 5 and max(data_list) > 100:
        results["status"] = "high_volume_high_value"
        results["avg"] = sum(data_list) / len(data_list)
    elif check_threshold(sum(data_list), min_val=20):
        results["status"] = "total_exceeds_limit"
        results["sum"] = sum(data_list)
    else:
        results["status"] = "normal_operation"
    return results
def main():
    sample_data = [15.5, 20.3, 89.1, 45.6, 120.7]
    if check_threshold(120.7):
        print("Threshold met for maximum value.")
    output = process_data(sample_data)
    print(f"Operation Status: {output['status']}")
if __name__ == '__main__':
    main()