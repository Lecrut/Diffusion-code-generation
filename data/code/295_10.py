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
        return None
    except ValueError:
        return "Invalid input"
if __name__ == '__main__':
    metric_length = 10.0
    imperial_length = 32.8084
    metric_weight = 5.0
    imperial_weight = 11.0231
    metric_volume = 1.0
    imperial_volume = 35.3147
    print(f"Metric Length: {metric_length}")
    print(f"Imperial Length (from Metric): {to_imperial_length(metric_length)}")
    print(f"Metric Length (from Imperial): {to_metric_length(imperial_length)}")
    print("-" * 20)
    print(f"Metric Weight: {metric_weight}")
    print(f"Imperial Weight (from Metric): {to_imperial_weight(metric_weight)}")
    print(f"Metric Weight (from Imperial): {to_metric_weight(imperial_weight)}")
    print("-" * 20)
    print(f"Metric Volume: {metric_volume}")
    print(f"Imperial Volume (from Metric): {to_imperial_volume(metric_volume)}")
    print(f"Metric Volume (from Imperial): {to_metric_volume(imperial_volume)}")
    print("-" * 20)
    invalid_input = "abc"
    result = safe_float_conversion(invalid_input, 'length')
    print(f"Testing invalid input '{invalid_input}' for length: {result}")