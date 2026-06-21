class NumberProcessor:
    @staticmethod
    def square_numbers(numbers):
        return [x**2 for x in numbers]

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5]
    squared_result = NumberProcessor.square_numbers(sample_numbers)
    print(squared_result)