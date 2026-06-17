import sys
from datetime import datetime
class FaultTolerantListExtractor:
    def __init__(self):
        self.log_level = "DEBUG"
        self.logger_name = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_extractor"
    def _log(self, message):
        timestamp = datetime.now().isoformat()
        log_entry = f"[{timestamp}] [{self.log_level}] {message}"
        print(log_entry)
    def extract_first_element_safe(self, data_list):
        self._log(f"Processing input: {data_list}")
        if not isinstance(data_list, list):
            error_msg = "Input must be a list."
            sys.stderr.write(f"{error_msg}\n")
            raise TypeError(error_msg)
        try:
            first_element = data_list[0]
            self._log(f"Successfully extracted element at index 0: {first_element}")
            return first_element
        except IndexError as e:
            error_msg = f"List is empty. Cannot extract first element."
            sys.stderr.write(f"{error_msg}\n")
            raise IndexError(error_msg) from e
def main():
    extractor = FaultTolerantListExtractor()
    sample_data_1 = [7, 2, "apple", None]
    sample_data_2 = []
    sample_data_3 = ["first_item"]
    print("--- Test Case A: Normal List ---")
    try:
        result_a = extractor.extract_first_element_safe(sample_data_1)
        print(f"Result: {result_a}")
    except Exception as e:
        print(f"Error in Test Case A: {e}")
    print("\n--- Test Case B: Empty List ---")
    try:
        result_b = extractor.extract_first_element_safe(sample_data_2)
        print(f"Result: {result_b}")
    except Exception as e:
        print(f"Error in Test Case B: {e}")
    print("\n--- Test Case C: Single Element List ---")
    try:
        result_c = extractor.extract_first_element_safe(sample_data_3)
        print(f"Result: {result_c}")
    except Exception as e:
        print(f"Error in Test Case C: {e}")
if __name__ == '__main__':
    main()