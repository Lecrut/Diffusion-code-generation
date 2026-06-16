def validate_and_execute(value: float) -> bool:
    if value < 0:
        return False
    thresholds = {10: "low", 50: "medium", 100: "high"}
    for threshold, label in sorted(thresholds.items()):
        if value >= threshold:
            print(f"Value {value} meets the '{label}' threshold.")
            return True
    print("No thresholds met.")
    return False
if __name__ == '__main__':
    test_values = [5, 20, 75, 150]
    for val in test_values:
        result = validate_and_execute(val)
        if not result and val >= 0:
            print(f"Warning: {val} is non-negative but no threshold was triggered.")