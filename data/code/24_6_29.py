def check_negative(number):
    if number < 0:
        return f"The entered value {number} is negative."
    else:
        return f"The entered value {number} is not negative."

if __name__ == '__main__':
    sample_values = [-5, 0, 10]
    for value in sample_values:
        print(check_negative(value))