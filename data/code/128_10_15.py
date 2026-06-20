def is_negative(number):
    if not isinstance(number, (int, float)):
        raise ValueError("Input must be a number")
    return number < 0

if __name__ == '__main__':
    sample_number = -15
    print(f"The sample number is: {sample_number}")
    print(f"Is the sample number negative? {is_negative(sample_number)}")

    sample_number_positive = 42
    print(f"The sample number is: {sample_number_positive}")
    print(f"Is the sample number negative? {is_negative(sample_number_positive)}")

    sample_number_zero = 0
    print(f"The sample number is: {sample_number_zero}")
    print(f"Is the sample number negative? {is_negative(sample_number_zero)}")