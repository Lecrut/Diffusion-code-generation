def swap_adjacent(values):
    if not isinstance(values, list):
        raise TypeError("Input must be a list.")
    for i in range(len(values) - 1):
        values[i], values[i + 1] = values[i + 1], values[i]
    return values
if __name__ == '__main__':
    sample_data = [5, 2, 8, 3, 9]
    try:
        result = swap_adjacent(sample_data)
        print("Swapped list:", result)
    except Exception as e:
        print(f"Error occurred: {e}")