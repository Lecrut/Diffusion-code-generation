import sys
from datetime import datetime
class FaultTolerantExtractor:
    def _log(self, level: str, message: str):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [{level.upper()}] {message}"
        print(log_entry)
    def extract_first_element(self, data_list: list) -> any:
        self._log("INFO", "Starting extraction process for input list.")
        if not isinstance(data_list, list):
            error_msg = f"Input must be a list. Received type: {type(data_list).__name__}"
            self._log("ERROR", error_msg)
            raise TypeError(error_msg)
        if len(data_list) == 0:
            warning_msg = "The provided list is empty."
            self._log("WARNING", warning_msg)
            return None
        try:
            first_element = data_list[0]
            success_msg = f"Successfully extracted element at index 0. Value type: {type(first_element).__name__}"
            self._log("INFO", success_msg)
            return first_element
        except IndexError as e:
            error_detail = str(e) + " - List length was insufficient."
            self._log("ERROR", error_detail)
            raise
def main():
    extractor = FaultTolerantExtractor()
    sample_data_1 = [42, 3.14, True]
    sample_data_2 = []
    sample_data_3 = ["apple", "banana"]
    invalid_input = (10,)
    print("--- Test Case 1: Normal List ---")
    try:
        result = extractor.extract_first_element(sample_data_1)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Exception occurred in Test Case 1: {e}")
    print("\n--- Test Case 2: Empty List ---")
    try:
        result = extractor.extract_first_element(sample_data_2)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Exception occurred in Test Case 2: {e}")
    print("\n--- Test Case 3: String List ---")
    try:
        result = extractor.extract_first_element(sample_data_3)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Exception occurred in Test Case 3: {e}")
    print("\n--- Test Case 4: Invalid Input Type ---")
    try:
        result = extractor.extract_first_element(invalid_input)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Exception occurred in Test Case 4: {e}")
if __name__ == '__main__':
    main()