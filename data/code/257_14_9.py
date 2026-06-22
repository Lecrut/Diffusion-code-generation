class ScoreCalculator:
    EMPTY_LIST_ERROR = "Input sequence cannot be empty"

    @staticmethod
    def calculate_difference(scores):
        if not scores:
            raise ValueError(ScoreCalculator.EMPTY_LIST_ERROR)
        return max(scores) - min(scores)

if __name__ == '__main__':
    calculator = ScoreCalculator()
    test_sequence_1 = [10, 5, 20, 3]
    result_1 = calculator.calculate_difference(test_sequence_1)
    print(f"Sequence: {test_sequence_1}, Difference: {result_1}")
    
    test_sequence_2 = (5.5, -2.1, 100.0, 0)
    result_2 = calculator.calculate_difference(test_sequence_2)
    print(f"Sequence: {test_sequence_2}, Difference: {result_2}")
    
    test_sequence_3 = [7]
    result_3 = calculator.calculate_difference(test_sequence_3)
    print(f"Sequence: {test_sequence_3}, Difference: {result_3}")
    
    test_sequence_4 = []
    try:
        calculator.calculate_difference(test_sequence_4)
    except ValueError as e:
        print(e)