def swap_adjacent(values):
    if not isinstance(values, list) and not (isinstance(values, tuple)):
        raise TypeError("Input must be a list or tuple.")
    for i in range(len(values) - 1):
        values[i], values[i + 1] = values[i + 1], values[i]
if __name__ == '__main__':
    sample_data = [5, 2, 8, 3, 9]
    try:
        swapped_result = swap_adjacent(sample_data)
        print(f"Original: {sample_data}")
        print(f"Swapped: {swapped_result}")
        if isinstance(swapped_result, list):
            sample_data[:] = swapped_result
    except Exception as e:
        print(f"Error occurred during processing: {e}")