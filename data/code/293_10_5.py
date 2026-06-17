import sys
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def metric_to_imperial(measurements):
    imperial_results = []
    for value in measurements:
        if isinstance(value, (int, float)):
            fahrenheit = celsius_to_fahrenheit(value)
            imperial_results.append(f"Celsius: {value}°C -> Fahrenheit: {fahrenheit:.2f}°F")
        else:
            imperial_results.append(f"Error: Invalid measurement type found: {value}")
    return imperial_results
if __name__ == '__main__':
    metric_measurements = [0, 100, 25, 37]
    print("--- Metric to Imperial Conversion ---")
    conversion_output = metric_to_imperial(metric_measurements)
    for result in conversion_output:
        print(result)