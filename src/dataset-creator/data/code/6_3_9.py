import json
import sys
from datetime import datetime
from typing import Any
class Logger:
    def __init__(self):
        self.log_file = "comparison_log.txt"
    def log(self, level: str, message: str) -> None:
        timestamp = datetime.now().isoformat()
        entry = f"[{timestamp}] [{level.upper()}] {message}\n"
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(entry)
logger = Logger()
def validate_object(obj: Any) -> bool:
    try:
        str_repr = repr(obj)
        if not isinstance(str_repr, str):
            return False
        logger.log("INFO", "Object representation generated successfully.")
        return True
    except Exception as e:
        logger.log("ERROR", f"Failed to generate object string representation. Error: {str(e)}")
        return False
def compare_objects(obj1: Any, obj2: Any) -> int:
    if not validate_object(obj1):
        raise ValueError(f"Invalid input for comparison 1.")
    if not validate_object(obj2):
        raise ValueError(f"Invalid input for comparison 2.")
    str_repr_1 = repr(obj1)
    str_repr_2 = repr(obj2)
    try:
        result_str = str_repr_1 > str_repr_2
        return int(result_str) if result_str else -int(result_str)
    except Exception as e:
        logger.log("ERROR", f"Comparison logic failed. Error: {str(e)}")
        raise
def main():
    sample_obj_a = {"id": 1, "name": "Alpha"}
    sample_obj_b = [30, 40]
    try:
        comparison_result = compare_objects(sample_obj_a, sample_obj_b)
        if comparison_result == 1:
            print(f"Object A is greater than Object B.")
        elif comparison_result == -1:
            print(f"Object B is greater than Object A.")
        else:
            logger.log("WARNING", "Objects are equal based on string representation.")
    except ValueError as ve:
        sys.stderr.write(f"{ve}\n")
        return 1
    except Exception as e:
        logger.log("CRITICAL", f"Unexpected error occurred. Error: {str(e)}")
        sys.exit(2)
    return 0
if __name__ == '__main__':
    sys.exit(main())