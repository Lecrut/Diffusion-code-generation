def extremes_diff(sequence):
    if not sequence:
        return 0
    highest = max(sequence)
    lowest = min(sequence)
    return highest - lowest

if __name__ == '__main__':
    test_sequence_1 = [3, 7, 2, 5]
    result_1 = extremes_diff(test_sequence_1)
    print(f"Sequence: {test_sequence_1}, Difference: {result_1}")
    
    test_sequence_2 = [-10, 10, -5, 5]
    result_2 = extremes_diff(test_sequence_2)
    print(f"Sequence: {test_sequence_2}, Difference: {result_2}")
    
    test_sequence_3 = [15]
    result_3 = extremes_diff(test_sequence_3)
    print(f"Sequence: {test_sequence_3}, Difference: {result_3}")
    
    test_sequence_4 = []
    result_4 = extremes_diff(test_sequence_4)
    print(f"Sequence: {test_sequence_4}, Difference: {result_4}")