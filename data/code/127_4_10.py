def is_odd(num):
    if not isinstance(num, int):
        raise ValueError("Invalid input type")
    return num % 2 == 1

if __name__ == '__main__':
    test_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    for value in test_values:
        try:
            result = is_odd(value)
            print(f"{value} is odd: {result}")
        except ValueError as e:
            print(e)