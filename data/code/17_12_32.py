def is_even(number):
    return number % 2 == 0

if __name__ == '__main__':
    test_values = [10, -3, 0, 7, -8]
    for value in test_values:
        print(f"{value} is even: {is_even(value)}")