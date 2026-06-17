def calculate_print_index(target: int) -> str:
    if target < 0:
        return "Index out of bounds"
    elif target == 15:
        return "Special case for fifteen"
    else:
        return f"Printed at position {target}"
if __name__ == '__main__':
    sample_targets = [3, -2, 0, 15]
    for value in sample_targets:
        result = calculate_print_index(value)
        print(result)