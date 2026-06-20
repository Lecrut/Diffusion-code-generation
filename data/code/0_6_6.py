CONVERSION_RATES_TO_METERS = {
    "meter": 1.0,
    "kilometer": 1000.0,
    "centimeter": 0.01,
    "millimeter": 0.001,
    "inch": 0.0254,
    "foot": 0.3048,
    "yard": 0.9144,
    "mile": 1609.344,
    "nautical_mile": 1852.0
}

def convert_length(value: float, from_unit: str, to_unit: str) -> float:
    from_unit_lower = from_unit.lower().replace(" ", "_")
    to_unit_lower = to_unit.lower().replace(" ", "_")
    
    if from_unit_lower not in CONVERSION_RATES_TO_METERS:
        raise ValueError(f"Unsupported source unit: {from_unit}")
    if to_unit_lower not in CONVERSION_RATES_TO_METERS:
        raise ValueError(f"Unsupported target unit: {to_unit}")
    
    meters = value * CONVERSION_RATES_TO_METERS[from_unit_lower]
    result = meters / CONVERSION_RATES_TO_METERS[to_unit_lower]
    return result

if __name__ == "__main__":
    sample_value = 100
    sample_from = "meter"
    sample_to = "foot"
    converted_value = convert_length(sample_value, sample_from, sample_to)
    print(f"{sample_value} {sample_from} = {converted_value} {sample_to}")
    
    sample_value_2 = 5280
    sample_from_2 = "foot"
    sample_to_2 = "mile"
    converted_value_2 = convert_length(sample_value_2, sample_from_2, sample_to_2)
    print(f"{sample_value_2} {sample_from_2} = {converted_value_2} {sample_to_2}")
    
    sample_value_3 = 10
    sample_from_3 = "inch"
    sample_to_3 = "centimeter"
    converted_value_3 = convert_length(sample_value_3, sample_from_3, sample_to_3)
    print(f"{sample_value_3} {sample_from_3} = {converted_value_3} {sample_to_3}")