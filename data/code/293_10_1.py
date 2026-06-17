import sys
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def metric_to_imperial(measurements):
    results = []
    for item in measurements:
        if isinstance(item, (int, float)):
            if item < -459.67:
                results.append({"original": item, "celsius": None, "fahrenheit": None})
            else:
                celsius = item
                fahrenheit = celsius_to_fahrenheit(celsius)
                results.append({"original": item, "celsius": celsius, "fahrenheit": fahrenheit})
        else:
            results.append({"original": item, "error": "Invalid data type"})
    return results
if __name__ == '__main__':
    metric_measurements = [100, 25, 37, -40]
    imperial_results = metric_to_imperial(metric_measurements)
    for result in imperial_results:
        print(f"Original Metric Value: {result['original']}")
        if result.get('celsius') is not None:
            print(f"  Celsius: {result['celsius']:.2f}")
            print(f"  Fahrenheit: {result['fahrenheit']:.2f}")
        else:
            print(f"  Error: {result.get('error', 'Unknown error')}")
        print("-" * 20)