class SequenceCalculator:
    @staticmethod
    def get_total(sequence):
        return sum(x for x in sequence)

if __name__ == '__main__':
    calculator = SequenceCalculator()
    sample_sequence_1 = [1.5, 2.3, 3.7, 4.1]
    result_1 = calculator.get_total(sample_sequence_1)
    print(f"The total for {sample_sequence_1} is: {result_1}")
    sample_sequence_2 = [-1.0, 2.5, -3.0, 4.5]
    result_2 = calculator.get_total(sample_sequence_2)
    print(f"The total for {sample_sequence_2} is: {result_2}")
    sample_sequence_3 = [0.0, 0.0, 0.0]
    result_3 = calculator.get_total(sample_sequence_3)
    print(f"The total for {sample_sequence_3} is: {result_3}")