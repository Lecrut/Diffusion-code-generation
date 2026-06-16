import math
def convert_measurements(data):
    results = {}
    for key, value in data.items():
        if key == "length":
            metric_value = value
            imperial_value = value * 1.012328
            results[f"{key}_metric"] = metric_value
            results[f"{key}_imperial"] = imperial_value
        elif key == "mass":
            metric_value = value
            imperial_value = value / 0.453592
            results[f"{key}_metric"] = metric_value
            results[f"{key}_imperial"] = imperial_value
        elif key == "temperature":
            celsius = value
            fahrenheit = celsius * 9/5 + 32
            results[f"{key}_metric"] = celsius
            results[f"{key}_imperial"] = fahrenheit
        else:
            results[f"{key}_metric"] = value
            results[f"{key}_imperial"] = value
    return results
if __name__ == '__main__':
    sample_data = {
        "length": 10.0,
        "mass": 75.0,
        "temperature": 25.0,
        "volume": 5.0
    }
    converted_data = convert_measurements(sample_data)
    print(converted_data)