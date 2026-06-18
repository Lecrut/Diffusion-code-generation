import json
import sys
from datetime import datetime
def safe_compare_objects(obj1: object, obj2: object) -> int:
    try:
        str_repr_1 = repr(obj1)
        str_repr_2 = repr(obj2)
        if not isinstance(str_repr_1, str):
            raise TypeError(f"Object 1 is not serializable to a standard string.")
        if not isinstance(str_repr_2, str):
            raise TypeError(f"Object 2 is not serializable to a standard string.")
        comparison = (str_repr_1 > str_repr_2) - ((str_repr_1 < str_repr_2))
        return int(comparison)
    except Exception as e:
        error_msg = f"Comparison failed for objects of type {type(obj1).__name__} and {type(obj2).__name__}: {e}"
        print(error_msg, file=sys.stderr)
        sys.exit(1)
def main():
    sample_obj_1 = {"id": 42, "data": [1.5, "text"]}
    sample_obj_2 = {"id": 30, "data": ["only", "strings"]}
    result = safe_compare_objects(sample_obj_1, sample_obj_2)
    if result > 0:
        print(f"Object 1 is greater than Object 2.")
    elif result < 0:
        print(f"Object 2 is greater than Object 1.")
    else:
        print("Objects are equal based on string representation.")
if __name__ == '__main__':
    main()