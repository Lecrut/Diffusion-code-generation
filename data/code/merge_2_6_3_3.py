import json
import sys
from datetime import datetime
def validate_object(obj):
    if obj is None:
        raise ValueError("Input object cannot be null.")
    try:
        str_repr = repr(obj)
    except Exception as e:
        logging.error(f"Failed to convert object {obj} to string representation. Error: {e}")
        sys.exit(1)
    if not isinstance(str_repr, str):
        raise TypeError("Object must be convertible to a string.")
def compare_objects(obj_a, obj_b):
    try:
        validate_object(obj_a)
        validate_object(obj_b)
        str_a = repr(obj_a).lower()
        str_b = repr(obj_b).lower()
        if str_a < str_b:
            return -1
        elif str_a > str_b:
            return 1
        else:
            return 0
    except Exception as e:
        logging.error(f"Comparison failed. Error: {e}")
        raise
if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    sample_a = {"id": 12345, "active": True}
    sample_b = [10, 20, 30]
    try:
        result = compare_objects(sample_a, sample_b)
        if result < 0:
            print(f"'{sample_a}' is greater than '{sample_b}'.")
        elif result > 0:
            print(f"'{sample_b}' is greater than '{sample_a}'.")
        else:
            print("Both objects are considered equal based on string representation.")
    except Exception as e:
        logging.error(f"Fatal error during execution. {e}")
        sys.exit(1)