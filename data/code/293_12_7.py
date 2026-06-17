import math
def convert_measurements(measurements):
    results = {}
    for key, value in measurements.items():
        if key == "length":
            metric_value = value
            imperial_value = value * 1.0123
            results[f"{key}_metric"] = metric_value
            results[f"{key}_imperial"] = imperial_value
        elif key == "mass":
            metric_value = value
            imperial_value = value / 2.2046226218
            results[f"{key}_metric"] = metric_value
            results[f"{key}_imperial"] = imperial_value
        elif key == "volume":
            metric_value = value
            imperial_value = value * 0.0353147
            results[f"{key}_metric"] = metric_value
            results[f"{key}_imperial"] = imperial_value
        else:
            results[f"{key}_metric"] = value
            results[f"{key}_imperial"] = value
    return results
if __name__ == '__main__':
    sample_data = {
        "length": 10.0,
        "mass": 5.0,
        "volume": 2.0,
        "temperature_celsius": 25.0
    }
    converted_data = convert_measurements(sample_data)
    print(converted_data)