SQUARE_FACTOR = 2

def square_numbers(numbers):
    return [x ** SQUARE_FACTOR for x in numbers]

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5]
    squared_result = square_numbers(sample_numbers)
    print(squared_result)