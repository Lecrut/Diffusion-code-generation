def convert_length(length: float, unit: str) -> float:
    conversions = {
        "meters": length,
        "feet": length * 3.28084,
        "kilometers": length * 1000.0
    }
    supported_units = set(conversions.keys())
    if unit in supported_units:
        return conversions[unit]
    else:
        raise ValueError(f"Unsupported unit: {unit}")
if __name__ == '__main__':
    length_m = 10.0
    unit_m = "meters"
    result_m = convert_length(length_m, unit_m)
    print(f"{length_m} meters is {result_m} in {unit_m}")
    length_ft = 10.0
    unit_ft = "feet"
    result_ft = convert_length(length_ft, unit_ft)
    print(f"{length_ft} meters is {result_ft} in {unit_ft}")
    length_km = 5.0
    unit_km = "kilometers"
    result_km = convert_length(length_km, unit_km)
    print(f"{length_km} meters is {result_km} in {unit_km}")
    try:
        convert_length(10.0, "miles")
    except ValueError as e:
        print(f"Caught expected error: {e}")