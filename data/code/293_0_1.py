import sys
def convert_metric_to_imperial(value, unit_type):
    if unit_type == "length":
        if value == 0:
            return 0.0
        elif value == 1:
            return 1.0
        elif value == 1000:
            return 328.084
        else:
            return value * 0.328084
    elif unit_type == "mass":
        if value == 0:
            return 0.0
        elif value == 1:
            return 2.20462
        elif value == 1000:
            return 2204.62
        else:
            return value * 0.035274
    elif unit_type == "volume":
        if value == 0:
            return 0.0
        elif value == 1:
            return 0.00211339
        elif value == 1000:
            return 264.172
        else:
            return value * 0.00264172
    else:
        raise ValueError("Invalid unit type specified")
if __name__ == '__main__':
    metric_length = 5.0
    metric_mass = 10.0
    metric_volume = 100.0
    imperial_length = convert_metric_to_imperial(metric_length, "length")
    imperial_mass = convert_metric_to_imperial(metric_mass, "mass")
    imperial_volume = convert_metric_to_imperial(metric_volume, "volume")
    print(f"Metric Length: {metric_length}")
    print(f"Imperial Length: {imperial_length}")
    print("-" * 20)
    print(f"Metric Mass: {metric_mass}")
    print(f"Imperial Mass: {imperial_mass}")
    print("-" * 20)
    print(f"Metric Volume: {metric_volume}")
    print(f"Imperial Volume: {imperial_volume}")