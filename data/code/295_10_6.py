import sys
def to_imperial_length(metric):
    return metric * 39.3701
def to_metric_length(imperial):
    return imperial / 39.3701
def to_imperial_weight(metric):
    return metric * 2.20462
def to_metric_weight(imperial):
    return imperial / 2.20462
def to_imperial_volume(metric):
    return metric * 0.0353147
def to_metric_volume(imperial):
    return imperial / 0.0353147
def safe_float_conversion(value, operation):
    try:
        num = float(value)
        if operation == 'length':
            if 'to_imperial' in operation:
                if 'length' in operation:
                    return num * 39.3701
                elif 'weight' in operation:
                    return num * 2.20462
                elif 'volume' in operation:
                    return num * 0.0353147
            else:
                if 'to_metric' in operation:
                    if 'length' in operation:
                        return num / 39.3701
                    elif 'weight' in operation:
                        return num / 2.20462
                    elif 'volume' in operation:
                        return num / 0.0353147
        else:
            raise ValueError("Invalid operation specified")
    except ValueError:
        return "Error: Invalid numeric input"
if __name__ == '__main__':
    sample_length_metric = 10.0
    sample_weight_imperial = 150.0
    sample_volume_metric = 5.0
    print("--- Length Conversion ---")
    print(f"Metric Length: {sample_length_metric}")
    imperial_length = to_imperial_length(sample_length_metric)
    print(f"Imperial Length: {imperial_length:.2f}")
    print("\n--- Weight Conversion ---")
    print(f"Metric Weight: {sample_weight_imperial}")
    metric_weight = to_metric_weight(sample_weight_imperial)
    print(f"Imperial Weight: {to_imperial_weight(sample_weight_imperial):.2f}")
    print("\n--- Volume Conversion ---")
    print(f"Metric Volume: {sample_volume_metric}")
    imperial_volume = to_imperial_volume(sample_volume_metric)
    print(f"Imperial Volume: {imperial_volume:.2f}")
    print("\n--- Input Validation Test (Non-numeric) ---")
    invalid_input = "abc"
    print(f"Attempting conversion with invalid input '{invalid_input}': {safe_float_conversion(invalid_input, 'length')}")
    invalid_input_2 = "10.5a"
    print(f"Attempting conversion with invalid input '{invalid_input_2}': {safe_float_conversion(invalid_input_2, 'weight')}")