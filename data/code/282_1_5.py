class SequenceSumCalculator:
    def __init__(self, data):
        self.data = data

    def calculate_sum(self):
        try:
            return sum(self.data)
        except TypeError as e:
            print(f"Error: {e}")
            return None

if __name__ == '__main__':
    sample_data = [1, 5, 10, 15, 20]
    calculator = SequenceSumCalculator(sample_data)
    result = calculator.calculate_sum()
    if result is not None:
        print(result)