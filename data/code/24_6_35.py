NEGATIVE_THRESHOLD = 0

def is_negative(number):
    return number < NEGATIVE_THRESHOLD

def check_negative_description(number):
    if is_negative(number):
        return f"The entered value {number} is negative."
    else:
        return f"The entered value {number} is not negative."

if __name__ == '__main__':
    sample_values = [-5, 0, 15]
    for value in sample_values:
        print(check_negative_description(value))