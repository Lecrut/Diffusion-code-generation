def convert_length(length, target_unit):
    supported_units = ["meters", "feet", "kilometers"]
    if target_unit not in supported_units:
        raise ValueError(f"Unsupported unit: {target_unit}")
    
    conversion_rates = {
        "meters": 1.0,
        "feet": 3.28084,
        "kilometers": 0.001
    }
    
    base_value = length / conversion_rates["meters"]
    result = base_value * conversion_rates[target_unit]
    return result

if __name__ == "__main__":
    sample_length = 100.0
    sample_unit = "feet"
    print(convert_length(sample_length, sample_unit))
    
    sample_length_2 = 5.0
    sample_unit_2 = "kilometers"
    print(convert_length(sample_length_2, sample_unit_2))
    
    sample_length_3 = 1000.0
    sample_unit_3 = "meters"
    print(convert_length(sample_length_3, sample_unit_3))