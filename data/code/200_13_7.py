def square_numbers(numbers):
    return list(map(lambda x: x**2, numbers))

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5]
    squared_result = square_numbers(sample_numbers)
    print(squared_result)