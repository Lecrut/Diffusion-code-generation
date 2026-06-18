from typing import List, Dict, Union, Optional
class MassConverter:
    @staticmethod
    def normalize_value(value: float) -> float:
        if isinstance(value, str):
            try:
                val = float(value)
            except ValueError:
                raise TypeError("Value must be a number.")
            unit_map = {"kg": 1, "g": 0.001, "lbs": 0.453592}
            if value.lower() in ["kg", "kilograms"]:
                return val * unit_map["kg"]
            elif value.lower() in ["g", "grams"]:
                return val * unit_map["g"]
            elif value.lower() in ["lbs", "pounds"]:
                return val * unit_map["lbs"]
        if isinstance(value, (int, float)):
            return value
        raise TypeError("Invalid mass format.")
    @staticmethod
    def calculate_difference(
        list_a: List[Union[float, str]], 
        list_b: Optional[List[Union[float, str]]] = None
    ) -> Dict[str, float]:
        if not isinstance(list_a, list):
            raise TypeError("First argument must be a list.")
        normalized_list = [MassConverter.normalize_value(item) for item in list_a]
        total_sum = sum(normalized_list)
        result: Dict[str, float] = {
            "total_difference_kg": 0.0,
            "individual_differences": []
        }
        if list_b is None or not isinstance(list_b, list):
            for val in normalized_list:
                result["individual_differences"].append(val)
            return result
        else:
            try:
                b_normalized = [MassConverter.normalize_value(item) for item in list_b]
                if len(list_a) != len(b_normalized):
                    raise ValueError("Lists must have the same length.")
                diffs = []
                for i, (a_val, b_val) in enumerate(zip(normalized_list, b_normalized)):
                    diff = a_val - b_val
                    result["individual_differences"].append({
                        "index": i, 
                        "value_a_kg": a_val, 
                        "value_b_kg": b_val, 
                        "difference_kg": diff
                    })
                result["total_difference_kg"] = abs(sum(normalized_list) - sum(b_normalized))
            except Exception as e:
                raise ValueError(f"Error calculating differences: {str(e)}") from e
        return result
if __name__ == '__main__':
    sample_data_a = [10, "5", 2.5]                                                                           
    sample_data_b = ["3 lbs", 7, "8"] 
    converter = MassConverter()
    try:
        diff_result = converter.calculate_difference(sample_data_a)
        print("Difference Result (vs Zero):")
        print(f"Total Difference: {diff_result['total_difference_kg']} kg")
        for item in diff_result["individual_differences"]:
            if isinstance(item, dict):                                                                                      
                pass 
    except Exception as e:
        print(f"Error occurred: {e}")
sample_list_1 = [50, "2", 4.5]                                                                                                              
sample_list_2 = ["3 lbs", 7, "8"]
try:
    final_result = MassConverter.calculate_difference(sample_list_1)
    print("Calculated Difference:")
    print(f"Total Difference (kg): {final_result['total_difference_kg']}")
except Exception as e:
    print(e)