import time
def validate_and_execute(value: float) -> bool:
    if value < 0:
        print("Value is negative.")
        return False
    elif value <= 10:
        print(f"Processing small value: {value}")
        return True
    else:
        print(f"Executing large operation for: {value}")
        time.sleep(2)
        return True
def check_thresholds(data_list: list[float]) -> dict[str, bool]:
    results = {"under_10": False, "over_50": False}
    has_negative = any(x < 0 for x in data_list)
    if not has_negative and all(0 <= x <= 10 for x in data_list):
        results["under_10"] = True
    elif sum(data_list) > 50:
        results["over_50"] = True
    return results
if __name__ == '__main__':
    sample_value = -5.2
    test_data = [3, 4, 7, 12, 60]
    validate_and_execute(sample_value)
    thresholds_result = check_thresholds(test_data)
    print(f"Threshold status: {thresholds_result}")