import sys
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def convert_metric_to_imperial(measurements):
    results = []
    for item in measurements:
        if isinstance(item, (int, float)):
            if item < -459.67:
                fahrenheit = celsius_to_fahrenheit(item)
                results.append({"original": item, "imperial": fahrenheit, "unit": "C to F"})
            elif item >= -459.67:
                results.append({"original": item, "imperial": item, "unit": "F (Assumed)"})
            else:
                results.append({"original": item, "imperial": item, "unit": "Unknown/Error"})
        elif isinstance(item, str):
            try:
                celsius = float(item)
                fahrenheit = celsius_to_fahrenheit(celsius)
                results.append({"original": celsius, "imperial": fahrenheit, "unit": "C to F"})
            except ValueError:
                results.append({"original": item, "imperial": None, "unit": "Invalid Input"})
        else:
            results.append({"original": item, "imperial": None, "unit": "Unsupported Type"})
    return results
if __name__ == '__main__':
    metric_measurements = [0.0, 25.0, 100.0, -40.0, 37.0]
    converted_data = convert_metric_to_imperial(metric_measurements)
    for data in converted_data:
        print(f"Original: {data['original']}, Imperial: {data['imperial']}, Conversion Type: {data['unit']}")