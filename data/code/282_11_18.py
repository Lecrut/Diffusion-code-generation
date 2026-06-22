class TotalCalculator:
    @staticmethod
    def calculate_total(numbers):
        try:
            return sum(numbers)
        except TypeError as e:
            print(f"Error: {e}")
            return None

if __name__ == '__main__':
    sample_numbers = (10, 20, 30, 40, 50)
    calculator = TotalCalculator()
    result = calculator.calculate_total(sample_numbers)
    print(result)