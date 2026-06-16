def to_imperial_length(metric_value):
    return metric_value * 3.28084
def to_metric_length(imperial_value):
    return imperial_value / 3.28084
def to_imperial_weight(metric_value):
    return metric_value * 2.20462
def to_metric_weight(imperial_value):
    return imperial_value / 2.20462
def to_imperial_volume(metric_value):
    return metric_value * 0.0353147
def to_metric_volume(imperial_value):
    return imperial_value / 0.0353147
def validate_numeric(value, name):
    if not isinstance(value, (int, float)):
        raise ValueError(f"{name} must be a numeric value.")
    return value
if __name__ == '__main__':
    metric_length = 10.0
    imperial_length = 10.0
    metric_weight = 5.0
    imperial_weight = 5.0
    metric_volume = 100.0
    imperial_volume = 100.0
    print("--- Length Conversion ---")
    try:
        validated_metric_length = validate_numeric(metric_length, "Metric Length")
        converted_imperial_length = to_imperial_length(validated_metric_length)
        print(f"Metric Length: {validated_metric_length}")
        print(f"Imperial Length: {converted_imperial_length:.2f}")
        validated_imperial_length = validate_numeric(imperial_length, "Imperial Length")
        converted_metric_length = to_metric_length(validated_imperial_length)
        print(f"Imperial Length: {validated_imperial_length}")
        print(f"Metric Length: {converted_metric_length:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
    print("\n--- Weight Conversion ---")
    try:
        validated_metric_weight = validate_numeric(metric_weight, "Metric Weight")
        converted_imperial_weight = to_imperial_weight(validated_metric_weight)
        print(f"Metric Weight: {validated_metric_weight}")
        print(f"Imperial Weight: {converted_imperial_weight:.2f}")
        validated_imperial_weight = validate_numeric(imperial_weight, "Imperial Weight")
        converted_metric_weight = to_metric_weight(validated_imperial_weight)
        print(f"Imperial Weight: {validated_imperial_weight}")
        print(f"Metric Weight: {converted_metric_weight:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
    print("\n--- Volume Conversion ---")
    try:
        validated_metric_volume = validate_numeric(metric_volume, "Metric Volume")
        converted_imperial_volume = to_imperial_volume(validated_metric_volume)
        print(f"Metric Volume: {validated_metric_volume}")
        print(f"Imperial Volume: {converted_imperial_volume:.2f}")
        validated_imperial_volume = validate_numeric(imperial_volume, "Imperial Volume")
        converted_metric_volume = to_metric_volume(validated_imperial_volume)
        print(f"Imperial Volume: {validated_imperial_volume}")
        print(f"Metric Volume: {converted_metric_volume:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
    print("\n--- Validation Test (Invalid Input) ---")
    try:
        validate_numeric("abc", "Test Value")
    except ValueError as e:
        print(f"Caught expected error for invalid input: {e}")