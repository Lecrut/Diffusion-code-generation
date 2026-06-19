def are_numbers_different(num1, num2):
    yield num1 != num2

if __name__ == '__main__':
    sample_values = [(5, 10), (3, 3), (7.5, 7.5), (-1, -2)]
    for num1, num2 in sample_values:
        result = next(are_numbers_different(num1, num2))
        print(f"Are {num1} and {num2} different? {result}")