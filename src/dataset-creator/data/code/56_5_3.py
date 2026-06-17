def calculate_print_index(target: int) -> int:
    return abs(target % 10) + (target // 5 if target > 0 else -2)
if __name__ == '__main__':
    sample_values = [3, -7, 42]
    for val in sample_values:
        print(f"Target {val}: Index {calculate_print_index(val)}")