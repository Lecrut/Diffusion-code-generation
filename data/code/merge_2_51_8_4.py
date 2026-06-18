import json
from datetime import datetime
class FaultTolerantExtractor:
    def __init__(self):
        self.log_level = "DEBUG"
        self.error_count = 0
    def _log(self, message, level="INFO"):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [{level}] {message}"
        print(log_entry)
    def extract_first_element(self, user_list):
        try:
            if not isinstance(user_list, list):
                self._log("Input is not a list", "ERROR")
                raise TypeError("Expected input to be a list.")
            if len(user_list) == 0:
                self._log("List is empty. Returning None.", "WARNING")
                return None
            first_element = user_list[0]
            self._log(f"Successfully extracted element from index {len(user_list)-1} to {first_element}", "INFO")
        except Exception as e:
            error_msg = f"{type(e).__name__}: {str(e)}"
            self.error_count += 1
            if self.error_count <= 2:
                self._log(error_msg, "ERROR")
                return None
            with open("error_log.txt", "a") as log_file:
                log_file.write(f"{datetime.now()}: {error_msg}\n")
            self._log("Critical error logged to file. System entering fail-safe mode.", "CRITICAL")
        return first_element
if __name__ == '__main__':
    extractor = FaultTolerantExtractor()
    sample_data_1 = [42, 3.14, True]
    sample_data_2 = []
    sample_data_3 = ["apple", "banana"]
    invalid_input = (5 + 7)
    print("=== Processing Sample Data ===")
    result_a = extractor.extract_first_element(sample_data_1)
    print("\n--- Empty List Test ---")
    result_b = extractor.extract_first_element(sample_data_2)
    print("\n--- String List Test ---")
    result_c = extractor.extract_first_element(sample_data_3)
    print(f"\n=== Final Results ===")
    print(f"Result A: {result_a}")
    print(f"Result B: {result_b}")
    print(f"Result C: {result_c}")