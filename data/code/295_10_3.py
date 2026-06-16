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
def safe_float_conversion(value, operation):
    try:
        num = float(value)
        if operation == 'length':
            if 'to_imperial' in operation:
                if 'length' in operation:
                    return to_imperial_length(num)
                elif 'weight' in operation:
                    return to_imperial_weight(num)
                elif 'volume' in operation:
                    return to_imperial_volume(num)
        elif operation == 'weight':
            if 'to_imperial' in operation:
                if 'length' in operation:
                    return to_imperial_length(num)
                elif 'weight' in operation:
                    return to_imperial_weight(num)
                elif 'volume' in operation:
                    return to_imperial_volume(num)
        elif operation == 'volume':
            if 'to_imperial' in operation:
                if 'length' in operation:
                    return to_imperial_length(num)
                elif 'weight' in operation:
                    return to_imperial_weight(num)
                elif 'volume' in operation:
                    return to_imperial_volume(num)
        else:
            return None
        return None
    except ValueError:
        return "Invalid input"
def convert_length(value, from_to):
    if not isinstance(value, (int, float)):
        return "Invalid input"
    if from_to == 'metric':
        if 'to_imperial' in from_to:
            if 'length' in from_to:
                return to_imperial_length(value)
            elif 'weight' in from_to:
                return to_imperial_weight(value)
            elif 'volume' in from_to:
                return to_imperial_volume(value)
    elif from_to == 'imperial':
        if 'to_metric' in from_to:
            if 'length' in from_to:
                return to_metric_length(value)
            elif 'weight' in from_to:
                return to_metric_weight(value)
            elif 'volume' in from_to:
                return to_metric_volume(value)
    return None
if __name__ == '__main__':
    sample_metric_length = 10.0
    sample_imperial_length = 32.8084
    sample_metric_weight = 5.0
    sample_imperial_weight = 11.0231
    sample_metric_volume = 1.0
    sample_imperial_volume = 0.0353147
    print("--- Length Conversion ---")
    print(f"Metric {sample_metric_length} to Imperial: {convert_length(sample_metric_length, 'metric')}")
    print(f"Imperial {sample_imperial_length} to Metric: {convert_length(sample_imperial_length, 'imperial')}")
    print("\n--- Weight Conversion ---")
    print(f"Metric {sample_metric_weight} to Imperial: {convert_length(sample_metric_weight, 'metric')}")
    print(f"Imperial {sample_imperial_weight} to Metric: {convert_length(sample_imperial_weight, 'imperial')}")
    print("\n--- Volume Conversion ---")
    print(f"Metric {sample_metric_volume} to Imperial: {convert_length(sample_metric_volume, 'metric')}")
    print(f"Imperial {sample_imperial_volume} to Metric: {convert_length(sample_imperial_volume, 'imperial')}")
    print("\n--- Input Validation Test ---")
    print(f"Attempting conversion with non-numeric length (string): {convert_length('abc', 'metric')}")
    print(f"Attempting conversion with non-numeric weight (float string): {convert_length('xyz', 'metric')}")