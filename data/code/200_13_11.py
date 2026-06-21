def square_numbers(numbers):
    return [x**2 for x in numbers]

if __name__ == '__main__':
    sample_numbers = [6, 7, 8, 9, 10]
    squared_result = square_numbers(sample_numbers)
    print(squared_result)