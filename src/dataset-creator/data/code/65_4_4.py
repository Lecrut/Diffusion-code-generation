class UnitConversionError(Exception):
    pass
def convert_length(value: float, from_unit: str, to_unit: str) -> float:
    base_meters = {
        "m": 1.0,
        "km": 1000.0,
        "cm": 0.01,
        "mm": 0.001,
        "mi": 1609.344,
        "yd": 0.9144,
        "ft": 0.3048,
        "in": 0.0254,
    }
    if from_unit not in base_meters or to_unit not in base_meters:
        raise UnitConversionError(f"Invalid unit: {from_unit} or {to_unit}")
    meters = value * base_meters[from_unit]
    return meters / base_meters[to_unit]
def vectorized_convert(lengths: list, from_units: str, to_units: str) -> list:
    if len(lengths) != 1:
        raise UnitConversionError("Vectorized mode requires single unit strings for batch processing")
    try:
        return [convert_length(l, f, t) for l in lengths]
    except Exception as e:
        raise UnitConversionError(f"Batch conversion failed: {e}")
if __name__ == '__main__':
    sample_data = [10.5, 2.34, 5000.0, 69.0]
    from_unit_str = "m"
    to_unit_str = "km"
    try:
        result = vectorized_convert(sample_data, from_unit_str, to_unit_str)
        print(result)
    except UnitConversionError as e:
        print(f"Error occurred: {e}")