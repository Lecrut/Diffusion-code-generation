def is_zero(number):
    return number == 0

if __name__ == '__main__':
    test_values = [1, 2, 3, 4, 5], [1, 0, 3, 4, 5], [7, 8, 9, 10], [0, 5, 10], []
    for values in test_values:
        result = any(is_zero(value) for value in values)
        print(f"Sequence {values}: {result}")