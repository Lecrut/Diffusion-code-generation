def convert_length(value: float, target_unit: str) -> float:
    conversion_factors = {
        "meters": 1.0,
        "feet": 3.28084,
        "kilometers": 0.001
    }
    
    if target_unit not in conversion_factors:
        raise ValueError(f"Unsupported unit: {target_unit}")
    
    base_meters = value / conversion_factors[target_unit]
    return base_meters * conversion_factors[target_unit]

def convert_to_base(value: float, source_unit: str) -> float:
    conversion_factors = {
        "meters": 1.0,
        "feet": 1.0 / 3.28084,
        "kilometers": 1000.0
    }
    
    if source_unit not in conversion_factors:
        raise ValueError(f"Unsupported unit: {source_unit}")
    
    return value * conversion_factors[source_unit]

def convert_from_base(value_meters: float, target_unit: str) -> float:
    conversion_factors = {
        "meters": 1.0,
        "feet": 3.28084,
        "kilometers": 0.001
    }
    
    if target_unit not in conversion_factors:
        raise ValueError(f"Unsupported unit: {target_unit}")
    
    return value_meters * conversion_factors[target_unit]

def convert_length(value: float, source_unit: str, target_unit: str) -> float:
    conversion_factors = {
        "meters": 1.0,
        "feet": 3.28084,
        "kilometers": 0.001
    }
    
    if source_unit not in conversion_factors:
        raise ValueError(f"Unsupported source unit: {source_unit}")
    
    if target_unit not in conversion_factors:
        raise ValueError(f"Unsupported target unit: {target_unit}")
    
    meters = value / conversion_factors[source_unit]
    result = meters * conversion_factors[target_unit]
    return result

if __name__ == '__main__':
    sample_value = 100
    sample_source = "meters"
    sample_target = "feet"
    
    result = convert_length(sample_value, sample_source, sample_target)
    print(result)
    
    sample_value_2 = 5.0
    sample_source_2 = "kilometers"
    sample_target_2 = "meters"
    
    result_2 = convert_length(sample_value_2, sample_source_2, sample_target_2)
    print(result_2)