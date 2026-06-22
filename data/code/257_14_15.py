class ScoreCalculator:
    DEFAULT_SEQUENCE = []

    @staticmethod
    def calculate_difference(sequence=DEFAULT_SEQUENCE):
        if not sequence:
            return 0
        return max(sequence) - min(sequence)

if __name__ == '__main__':
    calculator = ScoreCalculator()
    test_sequence_1 = [10, 5, 20, 3]
    print(f"Sequence: {test_sequence_1}, Difference: {calculator.calculate_difference(test_sequence_1)}")
    test_sequence_2 = (5.5, -2.1, 100.0, 0)
    print(f"Sequence: {test_sequence_2}, Difference: {calculator.calculate_difference(test_sequence_2)}")
    test_sequence_3 = [7]
    print(f"Sequence: {test_sequence_3}, Difference: {calculator.calculate_difference(test_sequence_3)}")
    test_sequence_4 = []
    print(f"Sequence: {test_sequence_4}, Difference: {calculator.calculate_difference(test_sequence_4)}")