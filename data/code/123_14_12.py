class SumCalculator:
    @staticmethod
    def calculate_sum(values):
        total = 0
        for value in values:
            try:
                number = int(value.strip())
                total += number
            except ValueError:
                print(f"Error: Invalid input '{value.strip()}' found. Skipping.")
        return total

if __name__ == '__main__':
    sample_input = [
        "10",
        "25",
        "hello",
        "30",
        "-5"
    ]
    calculator = SumCalculator()
    print(calculator.calculate_sum(sample_input))