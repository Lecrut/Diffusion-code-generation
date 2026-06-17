import sys
def find_print_index(data_list, target_value):
    try:
        if not isinstance(target_value, int) and not isinstance(target_value, float):
            raise TypeError("Target must be numeric.")
        for idx in range(len(data_list)):
            val = data_list[idx]
            sys.stderr.write(f"Checking index {idx}: value is {val}\n")
            if val == target_value:
                return f"Found at print index: {idx}"
        return "Target not found in list."
    except Exception as e:
        error_msg = f"Error during search: {str(e)}"
        sys.stderr.write(error_msg + "\n")
        raise
if __name__ == '__main__':
    sample_data = [10, 25, 30, 45, 60]
    target_to_find = 45
    result_message = find_print_index(sample_data, target_to_find)
    print(f"Result: {result_message}")