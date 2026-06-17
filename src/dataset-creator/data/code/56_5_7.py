def calculate_print_index(target: int) -> int:
    return abs(target % 10) + (target // 5 if target > 0 else -1)
if __name__ == '__main__':
    sample_values = [3, -7, 25]
    results = []
    for val in sample_values:
        index = calculate_print_index(val)
        print(f"Target {val}: Print Index {index}")