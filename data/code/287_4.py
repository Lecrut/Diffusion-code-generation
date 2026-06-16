import math
def calculate_average_weight(data):
    total_weight = 0.0
    total_value = 0.0
    for weight_str, unit in data:
        value = float(weight_str)
        if unit == 'kg':
            total_weight += value
        elif unit == 'lb':
            total_weight += value * 0.453592
        elif unit == 'g':
            total_weight += value / 1000.0
        else:
            raise ValueError(f"Unsupported unit: {unit}")
        total_value += value
    if not data:
        return 0.0
    average = total_weight / len(data)
    return average
if __name__ == '__main__':
    sample_data = [
        ("10", "kg"),
        ("22", "lb"),
        ("500", "g"),
        ("15.5", "kg")
    ]
    try:
        average = calculate_average_weight(sample_data)
        print(average)
    except ValueError as e:
        print(f"Error: {e}")