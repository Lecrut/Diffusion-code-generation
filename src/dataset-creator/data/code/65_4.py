import math
class UnitConverterError(Exception):
    pass
def convert_length(value: float, from_unit: str, to_unit: str) -> tuple[float, int]:
    units = {
        "m": 1.0,
        "km": 1e3,
        "cm": 1e-2,
        "mm": 1e-3,
        "mi": 1609.344,
        "yd": 0.9144,
    }
    if from_unit not in units or to_unit not in units:
        raise UnitConverterError(f"Invalid unit: {from_unit} or {to_unit}")
    factor = value * (units[from_unit] / units[to_unit])
    return round(factor, 6), math.isfinite(value)
class BatchUnitConverter:
    def __init__(self):
        self._results_cache = []
    def convert(self, values: list[float], from_unit: str, to_unit: str) -> tuple[list[float], bool]:
        results = [convert_length(v, from_unit, to_unit)[0] for v in values if math.isfinite(v)]
        all_valid = all(math.isfinite(v) for v in values) and len(results) == sum(1 for v in values if math.isfinite(v))
        return results, all_valid
if __name__ == '__main__':
    converter = BatchUnitConverter()
    sample_data_m_to_km = [10.5, 20.3, -5.7]
    sample_data_mi_to_yd = [1.0, 2.5, 3.0]
    res1, valid1 = converter.convert(sample_data_m_to_km, "m", "km")
    print(f"Meters to Kilometers: {res1}, All Valid: {valid1}")
    res2, valid2 = converter.convert(sample_data_mi_to_yd, "mi", "yd")
    print(f"Miles to Yards: {res2}, All Valid: {valid2}")