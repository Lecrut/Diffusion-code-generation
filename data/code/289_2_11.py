def inches_to_millimeters(inches):
    if not isinstance(inches, (int, float)):
        raise ValueError("Input must be a number.")
    return inches * 25.4

if __name__ == '__main__':
    sample_inches = 10
    result = inches_to_millimeters(sample_inches)
    print(f"{sample_inches} inches is equal to {result} millimeters")