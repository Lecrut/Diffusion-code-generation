def check_negative(number):
    return f"The number {number} is negative." if number < 0 else f"The number {number} is not negative."

if __name__ == '__main__':
    sample_values = [-10, 0, 25]
    for value in sample_values:
        print(check_negative(value))