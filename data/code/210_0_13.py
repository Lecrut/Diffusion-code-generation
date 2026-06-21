class MinMaxCalculator:
    @staticmethod
    def parse_numbers(data):
        return [float(x) for x in data.split()]

    @staticmethod
    def calculate_min_max(numbers):
        if not numbers:
            return None, None
        minimum = min(numbers)
        maximum = max(numbers)
        return minimum, maximum

if __name__ == '__main__':
    sample_data = "10 5 22 8 15 3"
    calculator = MinMaxCalculator()
    numbers = calculator.parse_numbers(sample_data)
    min_val, max_val = calculator.calculate_min_max(numbers)
    print(f"Minimum: {min_val}, Maximum: {max_val}")