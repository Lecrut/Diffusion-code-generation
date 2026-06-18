import sys
def swap_adjacent(values):
    if not isinstance(values, (list, tuple)):
        raise TypeError("Input must be a list or tuple.")
    n = len(values)
    for i in range(n - 1):
        temp = values[i]
        values[i], values[i + 1] = values[i + 1], temp
    return values
if __name__ == '__main__':
    sample_data = [5, 3, 8, 2, 9]
    try:
        result = swap_adjacent(sample_data)
        print(f"Original: {sample_data}")
        print(f"Swapped: {result}")
    except Exception as e:
        print(f"Error occurred: {e}", file=sys.stderr)