def calculate_print_index(target: int) -> int:
    return abs(target % 10)
if __name__ == '__main__':
    sample_targets = [5, -3, 27, 0]
    for target in sample_targets:
        index = calculate_print_index(target)
        print(f"Target {target}: Print Index {index}")