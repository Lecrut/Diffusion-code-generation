def check_negative(number):
    if number < 0:
        return f"The entered value {number} is negative."
    else:
        return f"The entered value {number} is not negative."

if __name__ == '__main__':
    sample_values = [-10, 0, 25]
    for value in sample_values:
        result = check_negative(value)
        print(result)