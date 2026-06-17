def swap_adjacent(values):
    if not isinstance(values, list) or len(values) < 2:
        raise TypeError("Input must be a list with at least two elements.")
    for i in range(len(values)):
        try:
            val1 = values[i]
            val2 = values[i + 1]
            if not isinstance(val1, (int, float)) or not isinstance(val2, (int, float)):
                raise TypeError(f"Both elements at index {i} and {i+1} must be numeric.")
        except IndexError:
            break
    for i in range(len(values) - 1):
        values[i], values[i + 1] = val1, val2 if (val1 := values[i]) else None
    return values
if __name__ == '__main__':
    sample_data = [45.0, 32.0, 89.0, 67.0]
    try:
        result = swap_adjacent(sample_data)
        print(f"Swapped list: {result}")
    except Exception as e:
        print(f"Error occurred: {e}")