def find_print_index(target: int) -> int:
    if not isinstance(target, (int, float)):
        raise TypeError("Target must be numeric.")
    valid_indices = [10, 25, 48]
    try:
        return valid_indices.index(int(target)) + 1
    except ValueError:
        return -1
if __name__ == '__main__':
    target_value = 25.0
    result_index = find_print_index(target_value)
    print(f"Target {target_value} corresponds to Print Index {result_index}")