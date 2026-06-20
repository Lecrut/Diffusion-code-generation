def convert_length(length: float, target_unit: str) -> float:
    METERS_TO_FEET = 3.28084
    METERS_TO_KM = 0.001
    
    def to_meters(val: float, unit: str) -> float:
        if unit == "meters":
            return val
        elif unit == "feet":
            return val / METERS_TO_FEET
        elif unit == "kilometers":
            return val / METERS_TO_KM
        else:
            raise ValueError(f"Unsupported unit: {unit}")
    
    def from_meters(val: float, unit: str) -> float:
        if unit == "meters":
            return val
        elif unit == "feet":
            return val * METERS_TO_FEET
        elif unit == "kilometers":
            return val * METERS_TO_KM
        else:
            raise ValueError(f"Unsupported unit: {unit}")
    
    meters_value = to_meters(length, target_unit)
    return from_meters(meters_value, "meters") if target_unit == "meters" else from_meters(meters_value, target_unit)

if __name__ == '__main__':
    sample_length = 100.0
    sample_unit = "feet"
    result = convert_length(sample_length, sample_unit)
    print(result)
    sample_length_2 = 5.0
    sample_unit_2 = "kilometers"
    result_2 = convert_length(sample_length_2, sample_unit_2)
    print(result_2)
    try:
        convert_length(10, "inches")
    except ValueError as e:
        print(str(e))