def square_numbers(numbers):
    return [x**2 for x in numbers]

if __name__ == '__main__':
    sample_values = [10, 15, 20, 25]
    squared_values = square_numbers(sample_values)
    print(squared_values)