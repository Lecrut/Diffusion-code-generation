class SumCalculator:
    def __init__(self, numbers):
        self.numbers = numbers

    def calculate_total(self):
        try:
            return sum(self.numbers)
        except TypeError as e:
            print(f"Error: {e}")
            return None

if __name__ == '__main__':
    sample_numbers = (10, 20, 30, 40, 50)
    calculator = SumCalculator(sample_numbers)
    result = calculator.calculate_total()
    print(result)