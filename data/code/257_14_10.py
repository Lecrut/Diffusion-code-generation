MAX_INT = float('inf')
MIN_INT = float('-inf')

def extremes_diff(sequence):
    if not sequence:
        return 0
    high = MIN_INT
    low = MAX_INT
    for score in sequence:
        if score > high:
            high = score
        if score < low:
            low = score
    return high - low

if __name__ == '__main__':
    test_sequence_1 = [10, 5, 20, 3]
    result_1 = extremes_diff(test_sequence_1)
    print(f"Sequence: {test_sequence_1}, Difference: {result_1}")
    test_sequence_2 = (5.5, -2.1, 100.0, 0)
    result_2 = extremes_diff(test_sequence_2)
    print(f"Sequence: {test_sequence_2}, Difference: {result_2}")
    test_sequence_3 = [7]
    result_3 = extremes_diff(test_sequence_3)
    print(f"Sequence: {test_sequence_3}, Difference: {result_3}")
    test_sequence_4 = []
    result_4 = extremes_diff(test_sequence_4)
    print(f"Sequence: {test_sequence_4}, Difference: {result_4}")