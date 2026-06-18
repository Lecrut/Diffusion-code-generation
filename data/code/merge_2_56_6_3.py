import sys
from datetime import datetime
def find_print_index(data_list: list, target_value) -> int:
    log_level = "INFO"
    if not data_list or len(data_list) == 0:
        sys.stderr.write(f"[LOG] ERROR: Input list is empty.\n")
        return -1
    start_time = datetime.now()
    search_start_index = 0
    found_index = -1
    def log_message(msg):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] [{log_level}] {msg}")
    log_message("Starting search for target value.")
    current_index = 0
    while current_index < len(data_list):
        if data_list[current_index] == target_value:
            found_index = current_index
            log_message(f"Target value '{target_value}' found at index {current_index}.")
            end_time = datetime.now()
            duration_ms = (end_time - start_time).total_seconds() * 1000
            log_message(f"Search completed in {duration_ms:.2f}ms.")
            return found_index
        current_index += 1
    end_time = datetime.now()
    duration_ms = (end_time - start_time).total_seconds() * 1000
    log_message(f"Target value '{target_value}' not found after scanning {current_index} elements. Duration: {duration_ms:.2f}ms.")
    return found_index
if __name__ == '__main__':
    sample_data = [3, 5, 7, 9, 11, 13]
    target_to_find = 9
    result_index = find_print_index(sample_data, target_to_find)
    if result_index != -1:
        print(f"Success: Value found at index {result_index}")
    else:
        print("Failure: Value not found")