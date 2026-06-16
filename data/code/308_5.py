class SequenceAnalyzer:
    @staticmethod
    def count_even_integers(sequence):
        count = 0
        for number in sequence:
            if number % 2 == 0:
                count += 1
        return count
if __name__ == '__main__':
    test_sequence_1 = [1, 2, 3, 4, 5, 6, 7, 8]
    result_1 = SequenceAnalyzer.count_even_integers(test_sequence_1)
    print(f"Sequence: {test_sequence_1}, Even count: {result_1}")
    test_sequence_2 = [10, 15, 22, 31, 40]
    result_2 = SequenceAnalyzer.count_even_integers(test_sequence_2)
    print(f"Sequence: {test_sequence_2}, Even count: {result_2}")
    test_sequence_3 = [1, 3, 5, 7, 9]
    result_3 = SequenceAnalyzer.count_even_integers(test_sequence_3)
    print(f"Sequence: {test_sequence_3}, Even count: {result_3}")
    test_sequence_4 = [2, 4, 6, 8, 10]
    result_4 = SequenceAnalyzer.count_even_integers(test_sequence_4)
    print(f"Sequence: {test_sequence_4}, Even count: {result_4}")