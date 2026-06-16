def calculate_average_weight(data):
    total_weight = 0
    total_unit_conversion_factor = 0
    for weight_str, unit in data:
        try:
            weight = float(weight_str)
            if unit == "kg":
                total_weight += weight
                total_unit_conversion_factor += 1
            elif unit == "lb":
                weight_in_kg = weight / 2.2046226218488
                total_weight += weight_in_kg
                total_unit_conversion_factor += 1
            else:
                raise ValueError(f"Unsupported unit: {unit}")
        except ValueError as e:
            raise ValueError(f"Invalid data format: {weight_str} {unit}. Error: {e}")
    if total_unit_conversion_factor == 0:
        return 0.0
    average_weight = total_weight / total_unit_conversion_factor
    return average_weight
if __name__ == '__main__':
    sample_data = [
        ("70.0", "kg"),
        ("150.0", "lb"),
        ("80.0", "kg"),
        ("200.0", "lb")
    ]
    try:
        average = calculate_average_weight(sample_data)
        print(average)
    except ValueError as e:
        print(f"Error: {e}")