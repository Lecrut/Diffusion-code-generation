import sys
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def metric_to_imperial(measurements):
    results = {}
    for item in measurements:
        if isinstance(item, tuple):
            value, unit = item
            if unit == 'C':
                fahrenheit = celsius_to_fahrenheit(value)
                results[f"{value} C"] = f"{fahrenheit:.2f} F"
            elif unit == 'F':
                results[f"{value} F"] = f"{value:.2f} F (No Conversion)"
            else:
                results[str(item)] = "Unknown Unit"
        elif isinstance(item, (int, float)):
            fahrenheit = celsius_to_fahrenheit(item)
            results[f"{item} C"] = f"{fahrenheit:.2f} F"
        else:
            results[str(item)] = "Invalid Type"
    return results
if __name__ == '__main__':
    sample_measurements = [
        (20, 'C'),
        (37.5, 'C'),
        (100, 'C'),
        (0, 'C'),
        (68, 'F')                                                         
    ]
    converted_data = metric_to_imperial(sample_measurements)
    for key, value in converted_data.items():
        print(f"{key}: {value}")