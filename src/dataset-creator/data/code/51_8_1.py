import sys
from datetime import datetime
from typing import List, Any, Optional
class FaultTolerantExtractor:
    def __init__(self):
        self.logger = Logger()
    def extract_first(self, data_list: List[Any]) -> Optional[Any]:
        try:
            if not isinstance(data_list, list):
                raise TypeError("Input must be a list")
            if len(data_list) == 0:
                return None
            first_element = data_list[0]
            self.logger.log_info(f"Successfully extracted element at index 0 from {len(data_list)} items", extra={"element": str(first_element)})
            return first_element
        except Exception as e:
            error_msg = f"Failed to extract element. Error type: {type(e).__name__}, Message: {str(e)}"
            self.logger.log_error(error_msg)
            raise
class Logger:
    def __init__(self):
        pass
    def log_info(self, message: str, extra: Optional[dict] = None):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        level = "INFO"
        if extra is not None and isinstance(extra.get("element"), (str, int)):
            element_str = f", Element found: {extra['element']}"
        else:
            element_str = ""
        log_line = f"[{timestamp}] [{level}] {message}{element_str}\n"
        sys.stdout.write(log_line)
        sys.stdout.flush()
    def log_error(self, message: str):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        level = "ERROR"
        log_line = f"[{timestamp}] [{level}] {message}\n"
        sys.stderr.write(log_line)
        sys.stderr.flush()
if __name__ == '__main__':
    extractor = FaultTolerantExtractor()
    sample_data_1: List[int] = [42, "hello", 3.14]
    sample_data_2: List[str] = ["apple", "banana"]
    sample_data_3: List[Any] = []
    invalid_input: Any = (10, 20)
    print("--- Test Case 1 ---")
    try:
        result = extractor.extract_first(sample_data_1)
        if result is not None:
            print(f"Result: {result}")
    except Exception as e:
        print(f"Exception occurred in test case 1: {e}", file=sys.stderr)
    print("--- Test Case 2 ---")
    try:
        result = extractor.extract_first(sample_data_2)
        if result is not None:
            print(f"Result: {result}")
    except Exception as e:
        print(f"Exception occurred in test case 2: {e}", file=sys.stderr)
    print("--- Test Case 3 ---")
    try:
        result = extractor.extract_first(sample_data_3)
        if result is None:
            print("Result: No element found (empty list)")
        else:
            print(f"Result: {result}")
    except Exception as e:
        print(f"Exception occurred in test case 3: {e}", file=sys.stderr)
    print("--- Test Case 4 ---")
    try:
        result = extractor.extract_first(invalid_input)
        if result is not None:
            print(f"Result: {result}")
    except Exception as e:
        print(f"Exception occurred in test case 4 (expected): {e}", file=sys.stderr)