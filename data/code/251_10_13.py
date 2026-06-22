class NumberAnalyzer:
    MAX_VALUE = float('inf')

    @staticmethod
    def determine_the_largest_number_present_calculate(numbers):
        if not numbers:
            return None
        largest = NumberAnalyzer.MAX_VALUE
        for number in numbers:
            if number > largest:
                largest = number
        return largest

if __name__ == '__main__':
    analyzer = NumberAnalyzer()
    sample_data = [42, 10, 99, 5, 123, 78]
    result = analyzer.determine_the_largest_number_present_calculate(sample_data)
    print(result)