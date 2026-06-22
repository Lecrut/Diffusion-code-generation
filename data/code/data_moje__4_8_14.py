import sys

def convert_distance(value, from_unit, to_unit):
    conversion_factors = {
        ("km", "miles"): 0.621371,
        ("miles", "km"): 1.60934
    }
    key = (from_unit.lower(), to_unit.lower())
    if key not in conversion_factors:
        raise ValueError(f"Unsupported conversion: {from_unit} to {to_unit}")
    return value * conversion_factors[key]

if __name__ == '__main__':
    sample_distance = 100
    sample_from = "km"
    sample_to = "miles"
    result = convert_distance(sample_distance, sample_from, sample_to)
    print(f"{sample_distance} {sample_from} equals {result} {sample_to}")
    sample_distance_back = result
    result_back = convert_distance(sample_distance_back, sample_to, sample_from)
    print(f"{sample_distance_back} {sample_to} equals {result_back} {sample_from}")