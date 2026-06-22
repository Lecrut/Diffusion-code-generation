def square_numbers(numbers):
    squared_values = []
    for number in numbers:
        squared_values.append(number ** 2)
    return squared_values

if __name__ == '__main__':
    sample_values = [7, 8, 9, 10, 11]
    result = square_numbers(sample_values)
    print(result)