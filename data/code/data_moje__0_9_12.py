import math

def convert_measurements(lengths, unit):
    conversions = {
        "kilometers": {"meters": 1000.0, "feet": 3280.84},
        "meters": {"meters": 1.0, "feet": 3.28084},
        "feet": {"meters": 0.3048, "feet": 1.0},
        "inches": {"meters": 0.0254, "feet": 0.0833333},
    }
    if unit not in conversions:
        raise ValueError(f"Unsupported unit: {unit}")
    factors = conversions[unit]
    results = []
    for length in lengths:
        meters = length * factors["meters"]
        feet = length * factors["feet"]
        results.append({"value": length, "unit": unit, "meters": meters, "feet": feet})
    return results

if __name__ == '__main__':
    sample_lengths = [1.0, 2.5, 10.0]
    sample_unit = "kilometers"
    converted = convert_measurements(sample_lengths, sample_unit)
    for item in converted:
        print(f"{item['value']} {item['unit']} is {item['meters']} meters and {item['feet']} feet")