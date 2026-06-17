def calculate_print_index(target: int) -> int:
    return abs(target % 10) + (target // 5 if target > 0 else -2)
if __name__ == '__main__':
    sample_values = [4, -7, 13]
    results = []
    for val in sample_values:
        index = calculate_print_index(val)
        results.append(f"Target {val}: Index {index}")
    print("\n".join(results))