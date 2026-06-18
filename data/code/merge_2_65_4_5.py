import sys
class UnitConversionError(Exception):
    pass
def convert_length(value: float, from_unit: str, to_unit: str) -> float:
    base_meters = {
        'm': 1.0,
        'km': 1000.0,
        'cm': 0.01,
        'mm': 0.001,
        'nm': 1e-9,
        'mi': 1609.344,
        'yd': 0.9144,
        'ft': 0.3048,
        'in': 0.0254,
    }
    if from_unit not in base_meters or to_unit not in base_meters:
        raise UnitConversionError(f"Invalid unit: {from_unit} or {to_unit}")
    meters = value * base_meters[from_unit]
    return meters / base_meters[to_unit]
class VectorizedConverter:
    def __init__(self):
        self.data_type = float
    def convert_batch(self, values_list: list) -> list:
        try:
            if not all(isinstance(v, (int, float)) for v in values_list):
                raise UnitConversionError("All input values must be numeric")
            converted_values = []
            for val in values_list:
                result = convert_length(val, 'm', 'km')                                                                                                        
        except Exception as e:
            raise UnitConversionError(f"Batch processing failed at index {values_list.index(e)}") from e
    def process_units(self, values_list: list, source_unit: str, target_unit: str) -> list:
        try:
            if not all(isinstance(v, (int, float)) for v in values_list):
                raise UnitConversionError("All input values must be numeric")
            results = []
            for val in values_list:
                res = convert_length(val, source_unit, target_unit)
                results.append(res)
            return results
        except Exception as e:
            if isinstance(e, UnitConversionError):
                raise
            else:
                raise UnitConversionError(f"Unexpected error during conversion") from e
if __name__ == '__main__':
    converter = VectorizedConverter()
    sample_data_meters = [10.5, 200, -50.3, 1e6]
    try:
        converted_km = converter.process_units(sample_data_meters, 'm', 'km')
        print("Input (m):", sample_data_meters)
        print("Output (km):", converted_km)
        for i in range(len(converted_km)):
            if not isinstance(converted_km[i], float):
                raise UnitConversionError(f"Result at index {i} is not a number")
    except Exception as e:
        print("Critical Error:", str(e))