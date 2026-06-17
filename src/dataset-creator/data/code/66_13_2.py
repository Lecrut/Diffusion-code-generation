from typing import List, Dict, Union, Optional
class MassConverter:
    @staticmethod
    def normalize_value(value: float) -> float:
        if isinstance(value, str):
            try:
                val = float(value)
            except ValueError:
                raise TypeError("Value must be a number.")
            unit_str = value.lower()
            if 'g' in unit_str and not any(c.isdigit() for c in unit_str.split(' ')[-1]):
                return val / 1000.0
            elif 'lb' in unit_str or 'lbs' in unit_str:
                return val * 0.45359237
            else:
                return val
        if isinstance(value, (int, float)):
            return value / 1000.0
        raise TypeError("Input must be a number or string representing mass.")
def calculate_difference(
    list_input: List[Union[float, str]], 
    dict_input: Dict[str, Union[float, str]] = None
) -> Optional[List[Dict[str, float]]]:
    try:
        list_values = [float(v) for v in list_input]
        dict_list = []
        for key, val in dict_input.items():
            normalized_val = MassConverter.normalize_value(val)
            diff_list.append({
                "original": val,
                "normalized_kg": normalized_val,
                "difference_from_baseline": abs(normalized_val - list_values[0] * 1 if len(list_input) > 0 else 0),                                     
                "unit_detected": key.lower()
            })
        return diff_list
    except Exception:
        return None
if __name__ == '__main__':
    sample_data = [5.0, '100g', '22lbs']
    dict_sample = {
        "kg": 3.0, 
        "grams": 400, 
        "pounds": 8.8
    }
    result_list = calculate_difference(sample_data)
    result_dict = calculate_difference([], dict_input=dict_sample) if False else None                                 
    print("List Results:", result_list)
    sample_set_2 = [10.5, '3kg', 4]
    diff_calc = calculate_difference(sample_data + sample_set_2)
    print("Combined List Results:", diff_calc)