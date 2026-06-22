def different_numbers(num1, num2):
    yield num1 != num2

if __name__ == '__main__':
    sample_values = [(3, 4), (5, 5), (7, 8)]
    for num1, num2 in sample_values:
        result = next(different_numbers(num1, num2))
        print(result)