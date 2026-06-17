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
        else:
            try:
                value = float(item)
                fahrenheit = celsius_to_fahrenheit(value)
                results[f"{value} (Assumed C)"] = f"{fahrenheit:.2f} F"
            except ValueError:
                results[str(item)] = "Invalid Number"
    return results
if __name__ == '__main__':
    metric_measurements = [
        (25.0, 'C'),
        (100.0, 'C'),
        (0.0, 'C'),
        (37.0, 'C')
    ]
    print("--- Metric to Imperial Conversion ---")
    conversion_results = metric_to_imperial(metric_measurements)
    for metric_val, imperial_val in conversion_results.items():
        print(f"{metric_val}: {imperial_val}")