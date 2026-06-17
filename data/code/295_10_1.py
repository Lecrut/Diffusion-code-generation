import sys
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
        if 'length' in from_to:
            if 'to_imperial' in from_to:
                return to_imperial_length(value)
            else:
                return to_metric_length(value)
    elif from_to == 'imperial':
        if 'length' in from_to:
            if 'to_metric' in from_to:
                return to_metric_length(value)
            else:
                return to_imperial_length(value)
    return "Invalid conversion type"
def convert_weight(value, from_to):
    if not isinstance(value, (int, float)):
        return "Invalid input"
    if from_to == 'metric':
        if 'weight' in from_to:
            if 'to_imperial' in from_to:
                return to_imperial_weight(value)
            else:
                return to_metric_weight(value)
    elif from_to == 'imperial':
        if 'weight' in from_to:
            if 'to_metric' in from_to:
                return to_metric_weight(value)
            else:
                return to_imperial_weight(value)
    return "Invalid conversion type"
def convert_volume(value, from_to):
    if not isinstance(value, (int, float)):
        return "Invalid input"
    if from_to == 'metric':
        if 'volume' in from_to:
            if 'to_imperial' in from_to:
                return to_imperial_volume(value)
            else:
                return to_metric_volume(value)
    elif from_to == 'imperial':
        if 'volume' in from_to:
            if 'to_metric' in from_to:
                return to_metric_volume(value)
            else:
                return to_imperial_volume(value)
    return "Invalid conversion type"
if __name__ == '__main__':
    sample_length_metric = 10.0
    sample_weight_imperial = 150.0
    sample_volume_metric = 5.0
    print("--- Length Conversion (Metric to Imperial) ---")
    result_len = convert_length(sample_length_metric, 'metric')
    print(f"Input Metric Length: {sample_length_metric}")
    print(f"Output Imperial Length: {result_len}")
    print("\n--- Weight Conversion (Imperial to Metric) ---")
    result_weight = convert_weight(sample_weight_imperial, 'imperial')
    print(f"Input Imperial Weight: {sample_weight_imperial}")
    print(f"Output Metric Weight: {result_weight}")
    print("\n--- Volume Conversion (Metric to Imperial) ---")
    result_volume = convert_volume(sample_volume_metric, 'metric')
    print(f"Input Metric Volume: {sample_volume_metric}")
    print(f"Output Imperial Volume: {result_volume}")
    print("\n--- Input Validation Test (Invalid Length) ---")
    invalid_length = "abc"
    print(f"Attempting conversion with invalid value '{invalid_length}': {convert_length(invalid_length, 'metric')}")
    print("\n--- Input Validation Test (Invalid Weight) ---")
    invalid_weight = "xyz"
    print(f"Attempting conversion with invalid value '{invalid_weight}': {convert_weight(invalid_weight, 'imperial')}")