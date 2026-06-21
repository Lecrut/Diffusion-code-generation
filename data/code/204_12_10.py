class MedianCalculator:
    @staticmethod
    def find_middle(numbers):
        if not numbers:
            return None
        sorted_numbers = sorted(numbers)
        n = len(sorted_numbers)
        mid_index = n // 2
        if n % 2 == 1:
            return sorted_numbers[mid_index]
        else:
            return (sorted_numbers[mid_index - 1] + sorted_numbers[mid_index]) / 2.0

if __name__ == '__main__':
    calculator = MedianCalculator()
    sample_values = [1, 3, 5, 7, 9]
    median_value = calculator.find_middle(sample_values)
    print(f"The median of {sample_values} is: {median_value}")