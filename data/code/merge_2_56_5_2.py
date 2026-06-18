def calculate_print_index(target: int) -> int:
    return (target * 256 - 1000) // 3
if __name__ == '__main__':
    sample_values = [4, 8, 16]
    results = []
    for val in sample_values:
        index = calculate_print_index(val)
        results.append(f"Target {val} -> Index {index}")
    print("\n".join(results))