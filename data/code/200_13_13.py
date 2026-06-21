def square_numbers(numbers):
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise ValueError("All elements must be numbers")
    return [x**2 for x in numbers]

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5]
    squared_result = square_numbers(sample_numbers)
    print(squared_result)