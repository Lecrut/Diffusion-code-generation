def square_numbers(numbers):
    return [x**2 for x in numbers]

if __name__ == '__main__':
    sample_values = [6, 7, 8, 9, 10]
    squared_values = square_numbers(sample_values)
    print(squared_values)