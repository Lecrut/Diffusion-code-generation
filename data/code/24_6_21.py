def check_negative(number):
    if number < 0:
        return f"The number {number} is negative."
    else:
        return f"The number {number} is not negative."

if __name__ == '__main__':
    sample_values = [-10, 0, 5]
    for value in sample_values:
        print(check_negative(value))