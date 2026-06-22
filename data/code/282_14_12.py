class SumCalculator:
    def __init__(self):
        self.total = 0

    def add_numbers(self, input_string):
        try:
            numbers = [float(x.strip()) for x in input_string.split(',')]
            self.total += sum(numbers)
            return self.total
        except ValueError:
            return "Error: Invalid input. Please ensure all entries are valid numbers."

if __name__ == '__main__':
    calculator = SumCalculator()
    sample_input1 = "10, 25.5, 3"
    result1 = calculator.add_numbers(sample_input1)
    print(f"Result after adding '{sample_input1}': {result1}")

    sample_input2 = "40, 5.5, 20, 3.14"
    result2 = calculator.add_numbers(sample_input2)
    print(f"Result after adding '{sample_input2}': {result2}")