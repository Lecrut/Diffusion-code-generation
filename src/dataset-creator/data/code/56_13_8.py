def calculate_print_index(target: int) -> int:
    return abs(target % 10)
if __name__ == '__main__':
    sample_targets = [42, -7, 99]
    for value in sample_targets:
        result_index = calculate_print_index(value)
        print(f"Target {value} -> Print Index {result_index}")