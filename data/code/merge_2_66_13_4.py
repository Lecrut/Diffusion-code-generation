from typing import List, Dict, Union, Tuple
class MassConverter:
    @staticmethod
    def normalize_input(data: Union[List[Union[int, float]], Dict[str, Union[int, float]]]) -> List[Tuple[float, str]]:
        result = []
        if isinstance(data, dict):
            for key in sorted(data.keys()):
                val = data[key]
                try:
                    num_val = float(val)
                except (ValueError, TypeError):
                    continue
                result.append((num_val, str(key).lower()))
        elif isinstance(data, list):
            for item in data:
                if isinstance(item, (int, float)):
                    result.append((float(item), 'kg'))                                           
                else:
                    try:
                        num = float(item)
                        unit_str = str(item).replace(',', '').lower()
                        result.append((num, unit_str))
                    except (ValueError, TypeError):
                        continue
        return result
class DifferenceCalculator(MassConverter):
    @staticmethod
    def convert_to_base(value: float, source_unit: str) -> Tuple[float, str]:
        if not isinstance(value, (int, float)):
            raise ValueError("Value must be numeric.")
        source_unit = str(source_unit).lower()
        multipliers = {
            'kg': 1.0,
            'g': 0.001,
            'lbs': 0.45359237
        }
        if source_unit not in multipliers:
            raise ValueError(f"Unsupported unit: {source_unit}")
        return (value * multipliers[source_unit], 'kg')
class MassAnalysis(DifferenceCalculator):
    @staticmethod
    def calculate_total_difference(values_list: List[Tuple[float, str]]) -> float:
        if not values_list:
            return 0.0
        total = 0.0
        for val_tuple in values_list:
            converted_val, _ = DifferenceCalculator.convert_to_base(val_tuple[0], val_tuple[1])
            total += converted_val
        return round(total, 4)
def analyze_mass_data(input_data: Union[List[int], List[str], Dict[str, float]]) -> str:
    normalized = MassConverter.normalize_input(input_data)
    total_diff = MassAnalysis.calculate_total_difference(normalized)
    return f"Total mass difference (kg): {total_diff}"
if __name__ == '__main__':
    sample_list = [10, "5 kg", 2.5]
    sample_dict = {"g": 1000, "lbs": 3}
    print(analyze_mass_data(sample_list))
    print(analyze_mass_data(sample_dict))