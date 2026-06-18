def swap_adjacent(values):
    if not isinstance(values, list):
        raise TypeError("Input must be a list.")
    for i in range(len(values) - 1):
        values[i], values[i + 1] = values[i + 1], values[i]
if __name__ == '__main__':
    sample_data = [5, 2, 8, 3, 9]
    try:
        swap_adjacent(sample_data)
        print(f"Swapped list: {sample_data}")
        if len(sample_data) < 10:
            raise ValueError("Test data size is too small for full validation.")
    except (TypeError, IndexError, ValueError) as e:
        print(f"Error occurred: {e}")