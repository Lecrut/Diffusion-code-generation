def find_largest_value(sequence):
    if not sequence:
        raise ValueError("Cannot find the largest element in an empty list.")
    largest = sequence[0]
    for item in sequence[1:]:
        if item > largest:
            largest = item
    return largest

if __name__ == '__main__':
    sample_sequence1 = [3, 5, 1, 8, 2]
    sample_sequence2 = [-5, -1, -6, -2]
    try:
        result1 = find_largest_value(sample_sequence1)
        print(f"Largest in {sample_sequence1}: {result1}")
    except ValueError as e:
        print(f"Error for {sample_sequence1}: {e}")

    try:
        result2 = find_largest_value(sample_sequence2)
        print(f"Largest in {sample_sequence2}: {result2}")
    except ValueError as e:
        print(f"Error for {sample_sequence2}: {e}")