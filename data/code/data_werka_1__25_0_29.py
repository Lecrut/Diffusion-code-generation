def is_exactly_zero(number):
    return number == 0

if __name__ == '__main__':
    test_values = [0, 1, -1, 0.0, -0.0, float('inf'), float('-inf')]
    for value in test_values:
        print(f"{value}: {is_exactly_zero(value)}")