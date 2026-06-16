import json
import sys
from datetime import datetime
def safe_compare_objects(obj1: object, obj2: object) -> int:
    try:
        str_repr_1 = repr(obj1)
        str_repr_2 = repr(obj2)
        if not isinstance(str_repr_1, str):
            raise TypeError("Object 1 must be convertible to a valid Python object.")
        if not isinstance(str_repr_2, str):
            raise TypeError("Object 2 must be convertible to a valid Python object.")
        comparison_result = -1
        try:
            comparison_result = (str_repr_1 > str_repr_2) - (str_repr_1 < str_repr_2)
        except TypeError as te:
            sys.stderr.write(f"Error during string comparison: {te}\n")
            return 0
        if comparison_result == 1:
            result = "greater"
        elif comparison_result == -1:
            result = "less"
        else:
            result = "equal"
    except Exception as e:
        sys.stderr.write(f"Fatal error in safe_compare_objects: {e}\n")
        return 0
    logging_output = f"[{datetime.now().isoformat()}] Compared '{str_repr_1}' vs '{str_repr_2}': Result is {result}"
    print(logging_output)
    return comparison_result
if __name__ == '__main__':
    sample_obj_a = {"key": "value", "nested": [1, 2, 3]}
    sample_obj_b = {"key": "other_value", "nested": [4, 5, 6]}
    try:
        result_code = safe_compare_objects(sample_obj_a, sample_obj_b)
        if result_code == -1:
            print("Object A is less than Object B.")
        elif result_code == 0:
            print("Objects are equal based on string representation.")
        else:
            print("Object A is greater than Object B.")
    except Exception as e:
        sys.stderr.write(f"Unhandled exception in main block: {e}\n")