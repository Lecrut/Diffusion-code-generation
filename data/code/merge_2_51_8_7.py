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
            success_msg = f"Successfully extracted element at index 0. Value: {first_element}"
            self._log("INFO", success_msg)
            return first_element
        except IndexError as e:
            error_detail = str(e)
            failure_msg = "Failed to extract element due to list bounds."
            self._log("ERROR", f"{failure_msg} Details: {error_detail}")
            raise
if __name__ == '__main__':
    extractor = FaultTolerantExtractor()
    sample_data_1 = [42, 3.14, "hello"]
    sample_data_2 = []
    sample_data_3 = ["apple", "banana", "cherry"]
    test_cases = [sample_data_1, sample_data_2, sample_data_3]
    for i, data in enumerate(test_cases):
        print(f"\n--- Processing Test Case {i+1} ---")
        try:
            result = extractor.extract_first_element(data)
            if result is not None:
                print(f"Result: {result}")
            else:
                print("No element extracted.")
        except Exception as e:
            print(f"Exception occurred for Test Case {i+1}: {e}")