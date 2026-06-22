def is_negative(number):
    if number < 0:
        return f"The value {number} is negative."
    else:
        return f"The value {number} is not negative."

if __name__ == '__main__':
    test_values = [-5, 0, 15]
    for value in test_values:
        print(is_negative(value))