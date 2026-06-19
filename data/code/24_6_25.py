def check_negative(number):
    if number < 0:
        return f"The number {number} is negative."
    else:
        return f"The number {number} is not negative."

if __name__ == '__main__':
    sample_value = -5
    result = check_negative(sample_value)
    print(result)