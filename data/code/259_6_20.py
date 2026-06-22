class NumberProcessor:
    @staticmethod
    def parse_numbers(numbers_str):
        return [int(num) for num in numbers_str.split(',')]

    @staticmethod
    def find_extremes(numbers):
        smallest = min(numbers)
        largest = max(numbers)
        return smallest, largest

if __name__ == '__main__':
    sample_values = "3,1,4,1,5,9,2,6,5,3,5"
    numbers = NumberProcessor.parse_numbers(sample_values)
    result = NumberProcessor.find_extremes(numbers)
    print(result)