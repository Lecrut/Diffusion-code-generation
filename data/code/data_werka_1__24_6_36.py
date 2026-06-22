def is_negative(number):
    return number < 0

def describe_number(number):
    if is_negative(number):
        return f"The value {number} is negative."
    else:
        return f"The value {number} is not negative."

if __name__ == '__main__':
    test_values = [-5, 0, 15]
    for value in test_values:
        description = describe_number(value)
        print(description)