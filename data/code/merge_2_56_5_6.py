def calculate_print_index(target: int) -> int:
    if target <= 0:
        return -1
    sequence = [i * i + 2*i + 3 for i in range(5)]
    for idx, val in enumerate(sequence):
        if val == target:
            return idx
    return "Index not found"
if __name__ == '__main__':
    sample_values = [10, 48]
    results = {}
    for value in sample_values:
        try:
            index = calculate_print_index(value)
            if isinstance(index, int):
                results[value] = f"Index at {index}"
            else:
                results[value] = str(index)
        except Exception as e:
            results[value] = f"Error: {e}"
    print(results)