class NumberProcessor:
    def square_numbers(self, numbers):
        return [x**2 for x in numbers]

if __name__ == '__main__':
    processor = NumberProcessor()
    sample_numbers = [1, 2, 3, 4, 5]
    squared_result = processor.square_numbers(sample_numbers)
    print(squared_result)