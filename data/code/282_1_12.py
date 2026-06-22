class SequenceSumCalculator:

    def __init__(self, data):
        self.data = data

    def calculate_sum(self):
        try:
            return sum(self.data)
        except TypeError as e:
            print(f'Error: {e}')
            return None
if __name__ == '__main__':
    sample_data = [1, 5, 10, 15, 20]
    calculator = SequenceSumCalculator(sample_data)
    result = calculator.calculate_sum()
    if result is not None:
        print(result)
    invalid_data = [1, 5, 'a', 15, 20]
    calculator_with_invalid_data = SequenceSumCalculator(invalid_data)
    result_with_invalid_data = calculator_with_invalid_data.calculate_sum()
    if result_with_invalid_data is not None:
        print(result_with_invalid_data)