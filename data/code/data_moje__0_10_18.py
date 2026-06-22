CONVERSION_RATES = {
    "meters": 1.0,
    "feet": 0.3048,
    "kilometers": 1000.0
}

def convert_length(length, target_unit):
    if target_unit not in CONVERSION_RATES:
        raise ValueError(f"Unsupported unit: {target_unit}")
    
    value_in_meters = length * CONVERSION_RATES[target_unit]
    return value_in_meters

if __name__ == "__main__":
    sample_length = 10
    target = "feet"
    result = convert_length(sample_length, target)
    print(result)