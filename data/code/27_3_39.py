def are_numbers_different(num1, num2):
    yield num1 != num2

if __name__ == '__main__':
    sample_values = [(1, 2), (3, 3), (5, 7)]
    for num1, num2 in sample_values:
        result = next(are_numbers_different(num1, num2))
        print(result)