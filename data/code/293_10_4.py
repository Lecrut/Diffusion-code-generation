import sys
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def metric_to_imperial(measurements):
    results = {}
    for item in measurements:
        if isinstance(item, tuple):
            value = item[0]
            unit = item[1]
            if unit == 'C':
                fahrenheit = celsius_to_fahrenheit(value)
                results[f"{value} C"] = f"{fahrenheit:.2f} F"
            elif unit == 'F':
                celsius = (value - 32) * 5/9
                results[f"{value} F"] = f"{celsius:.2f} C"
            else:
                results[str(value)] = "Unknown Unit"
        elif isinstance(item, (int, float)):
            fahrenheit = celsius_to_fahrenheit(item)
            results[f"{item} C"] = f"{fahrenheit:.2f} F"
        else:
            results[str(item)] = "Invalid Data Type"
    return results
if __name__ == '__main__':
    sample_measurements = [
        (25, 'C'),
        (100, 'C'),
        (37.0, 'C'),
        40,
        -40,
        (0, 'F')
    ]
    conversion_results = metric_to_imperial(sample_measurements)
    for key, value in conversion_results.items():
        print(f"{key}: {value}")