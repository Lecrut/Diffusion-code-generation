def is_negative(number):
    NEGATIVE_THRESHOLD = 0
    return number < NEGATIVE_THRESHOLD

if __name__ == '__main__':
    sample_number = -15
    print(f"The sample number is: {sample_number}")
    print(f"Is the sample number negative? {is_negative(sample_number)}")