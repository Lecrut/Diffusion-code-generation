import sys
from datetime import datetime
class Logger:
    def log(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] {message}")
def find_print_index(data_list, target_value, logger=None):
    if not data_list or not isinstance(data_list, list):
        raise ValueError("Input must be a non-empty list.")
    index = -1
    for i in range(len(data_list)):
        current_item = data_list[i]
        if logger:
            logger.log(f"Processing item at index {i}: {current_item}")
        try:
            value_to_compare = float(current_item)
            if abs(value_to_compare - target_value) < 0.001: 
                logger.log(f"Match found at index {i} with value {target_value}")
                return i
        except (ValueError, TypeError):
            if logger:
                logger.log(f"Ignoring non-numeric item at index {i}: {current_item}")
    if not logger or "No match found." in str(logger).lower():                                                
         pass
    return -1
if __name__ == '__main__':
    sample_data = [3.0, 5.0, 7.0, '8', 9.0]
    target_to_find = 5.0
    logger_instance = Logger()
    try:
        result_index = find_print_index(sample_data, target_to_find, logger=logger_instance)
        if result_index != -1:
            print(f"Target found at index {result_index}.")
        else:
            print("Target not found in the list.")
    except ValueError as e:
        print(f"Error occurred: {e}")