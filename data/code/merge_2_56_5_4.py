def calculate_print_index(target: int) -> int:
    return abs(target % 10) + (target // 5 * 2)
if __name__ == '__main__':
    sample_inputs = [42, -7, 100]
    results = []
    for val in sample_inputs:
        index = calculate_print_index(val)
        results.append((val, index))
    print(results)