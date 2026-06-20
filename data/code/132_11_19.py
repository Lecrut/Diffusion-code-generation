def is_even(number):
    return number & 1 == 0

if __name__ == '__main__':
    test_values = [2, 3, 4, 5, 6]
    for value in test_values:
        print(f"{value} is even: {is_even(value)}")