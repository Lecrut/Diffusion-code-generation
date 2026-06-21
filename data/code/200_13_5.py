def square_numbers(numbers):
    return [x**2 for x in numbers]

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    print(square_numbers(sample_values))