def square_numbers(numbers):
    squared_values = []
    for number in numbers:
        squared_values.append(number ** 2)
    return squared_values

if __name__ == '__main__':
    sample_values = [1, 3, 5, 7, 9]
    result = square_numbers(sample_values)
    print(result)