def to_imperial_length(metric):
    return metric * 3.28084
def to_metric_length(imperial):
    return imperial / 3.28084
def to_imperial_weight(metric):
    return metric * 2.20462
def to_metric_weight(imperial):
    return imperial / 2.20462
def to_imperial_volume(metric):
    return metric * 0.0353147
def to_metric_volume(imperial):
    return imperial / 0.0353147
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
    try:
        validated_metric_length = validate_numeric(metric_length, "Metric Length")
        validated_imperial_length = validate_numeric(imperial_length, "Imperial Length")
        validated_metric_weight = validate_numeric(metric_weight, "Metric Weight")
        validated_imperial_weight = validate_numeric(imperial_weight, "Imperial Weight")
        validated_metric_volume = validate_numeric(metric_volume, "Metric Volume")
        validated_imperial_volume = validate_numeric(imperial_volume, "Imperial Volume")
        print("--- Length Conversion ---")
        print(f"Metric {validated_metric_length} meters to Imperial: {to_imperial_length(validated_metric_length):.2f} feet")
        print(f"Imperial {validated_imperial_length} feet to Metric: {to_metric_length(validated_imperial_length):.2f} meters")
        print("\n--- Weight Conversion ---")
        print(f"Metric {validated_metric_weight} kg to Imperial: {to_imperial_weight(validated_metric_weight):.2f} lbs")
        print(f"Imperial {validated_imperial_weight} lbs to Metric: {to_metric_weight(validated_imperial_weight):.2f} kg")
        print("\n--- Volume Conversion ---")
        print(f"Metric {validated_metric_volume} liters to Imperial: {to_imperial_volume(validated_metric_volume):.2f} gallons")
        print(f"Imperial {validated_imperial_volume} gallons to Metric: {to_metric_volume(validated_imperial_volume):.2f} liters")
    except ValueError as e:
        print(f"Error: {e}")