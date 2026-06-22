def is_even(number):
    if number < 0:
        return is_even(~number)
    return (number & 1) == 0

if __name__ == '__main__':
    test_values = [2, 3, 0, -4, -5]
    for val in test_values:
        print(is_even(val))