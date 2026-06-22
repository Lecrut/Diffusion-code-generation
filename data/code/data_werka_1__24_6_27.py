def check_negative(number):
    return f"The number {number} is negative." if number < 0 else f"The number {number} is not negative."

if __name__ == '__main__':
    test_values = [-10, 0, 5]
    for value in test_values:
        print(check_negative(value))