def swap_adjacent(values):
    if not isinstance(values, list) and not hasattr(values, "__iter__"):
        raise TypeError("Input must be an iterable sequence.")
    try:
        values = list(values)
    except Exception as e:
        raise ValueError(f"Failed to convert input to a list: {e}")
    if len(values) < 2:
        return "Error: List must contain at least two elements."
    for i in range(0, len(values), 2):
        try:
            temp = values[i]
            values[i] = values[i + 1]
            values[i + 1] = temp
        except IndexError as e:
            return f"Error: Index out of bounds during swap. {e}"
    return values
if __name__ == '__main__':
    sample_data = [5, 3, 8, 2, 9, 4]
    result = swap_adjacent(sample_data)
    print(result)