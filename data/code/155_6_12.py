class SumCalculator:
    @staticmethod
    def sum_numbers(input_string):
        numbers = input_string.split()
        total_sum = 0
        for num_str in numbers:
            try:
                number = int(num_str)
                total_sum += number
            except ValueError:
                print(f"Error: Could not convert '{num_str}' to an integer.")
        return total_sum

if __name__ == '__main__':
    sample_input = "10 20 30 40"
    calculator = SumCalculator()
    result = calculator.sum_numbers(sample_input)
    print(result)