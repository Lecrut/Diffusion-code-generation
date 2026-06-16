class SequenceCalculator:
    def get_total(self, sequence):
        total = 0
        for element in sequence:
            total += element
        return total
if __name__ == '__main__':
    calculator = SequenceCalculator()
    sample_sequence_1 = [1, 2, 3, 4, 5]
    result_1 = calculator.get_total(sample_sequence_1)
    print(f"The total for {sample_sequence_1} is: {result_1}")
    sample_sequence_2 = [10, 20, 30, 40]
    result_2 = calculator.get_total(sample_sequence_2)
    print(f"The total for {sample_sequence_2} is: {result_2}")
    sample_sequence_3 = [-1, 5, -3, 10]
    result_3 = calculator.get_total(sample_sequence_3)
    print(f"The total for {sample_sequence_3} is: {result_3}")