def calculate_average_weight(data):
    total_weight = 0.0
    total_value = 0.0
    for weight_str, unit in data:
        value = float(weight_str)
        if unit == "kg":
            converted_value = value
        elif unit == "lb":
            converted_value = value * 0.453592
        else:
            raise ValueError(f"Unsupported unit: {unit}")
        total_weight += converted_value
        total_value += 1
    if total_value == 0:
        return 0.0
    average = total_weight / total_value
    return average
if __name__ == '__main__':
    sample_data = [
        ("10.0", "kg"),
        ("22.0", "lb"),
        ("5.5", "kg"),
        ("15.0", "lb")
    ]
    average = calculate_average_weight(sample_data)
    print(average)