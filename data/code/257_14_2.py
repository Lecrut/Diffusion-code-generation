def extremes_diff(sequence):
    if not sequence:
        raise ValueError("Input sequence cannot be empty")
    return max(sequence) - min(sequence)
if __name__ == '__main__':
    test_sequence_1 = [1, 5, 2, 8, 3]
    result_1 = extremes_diff(test_sequence_1)
    print(f"Sequence: {test_sequence_1}, Difference: {result_1}")
    test_sequence_2 = (100, -50, 0, 75)
    result_2 = extremes_diff(test_sequence_2)
    print(f"Sequence: {test_sequence_2}, Difference: {result_2}")
    test_sequence_3 = [42]
    result_3 = extremes_diff(test_sequence_3)
    print(f"Sequence: {test_sequence_3}, Difference: {result_3}")
    test_sequence_4 = []
    try:
        extremes_diff(test_sequence_4)
    except ValueError as e:
        print(f"Error for empty sequence: {e}")