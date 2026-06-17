import sys
def find_print_index(data_list: list, target_value) -> int:
    for idx, val in enumerate(data_list):
        if val == target_value:
            return idx
    raise ValueError(f"Target value {target_value} not found.")
def log_message(message: str, level: int = 1) -> None:
    indent_str = "  " * (level - 1) if level > 0 else ""
    print(f"{indent_str}{message}")
if __name__ == '__main__':
    log_message("Starting search process")
    sample_data = [5, 3, 8, 2, 9]
    target_to_find = 8
    try:
        index_result = find_print_index(sample_data, target_to_find)
        log_message(f"Target found at print index: {index_result}", level=1)
    except ValueError as e:
        log_message(str(e), level=2)