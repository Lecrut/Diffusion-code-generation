from typing import List, Dict, Union, Optional
class MassConverter:
    @staticmethod
    def normalize_value(value: float) -> float:
        if isinstance(value, (int, float)):
            return value / 1000 if value < 1 else value
        unit = str(type(value)).lower()
        try:
            val = float(value)
            if isinstance(val, (int, float)):
                return val
            raise ValueError("Unsupported input type")
        except Exception as e:
            print(f"Error normalizing value {value}: {e}")
    @staticmethod
    def convert_to_kilograms(value: Union[float, int]) -> float:
        if isinstance(value, float):
            return value
        unit = str(type(value)).lower()
        try:
            val = float(value)
            if isinstance(val, (int, float)):
                return val
            raise ValueError("Unsupported input type")
        except Exception as e:
            print(f"Error converting value {value}: {e}")
    @staticmethod
    def calculate_difference(values: List[Union[float, int]]) -> Dict[str, Union[int, float]]:
        normalized = [MassConverter.normalize_value(v) for v in values]
        return {
            "total_kg": round(sum(normalized), 2),
            "average_kg": round(sum(normalized) / len(values), 2) if values else 0,
            "count": len(values)
        }
def process_mass_data(input_list: List[Union[float, int]]) -> Dict[str, Union[int, float]]:
    return MassConverter.calculate_difference(input_list)
if __name__ == '__main__':
    sample_data = [1000, "5", 2.2]
    result = process_mass_data(sample_data)
    print(result["total_kg"])