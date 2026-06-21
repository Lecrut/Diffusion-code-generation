def find_largest_value(sequence):
    if not sequence:
        raise ValueError("Cannot find the largest element in an empty list.")
    largest = sequence[0]
    for item in sequence[1:]:
        if item > largest:
            largest = item
    return largest

if __name__ == '__main__':
    sample_sequence = [4, 7, 2, 9, 5]
    try:
        result = find_largest_value(sample_sequence)
        print(f"The largest element in {sample_sequence} is: {result}")
    except ValueError as e:
        print(f"Error: {e}")