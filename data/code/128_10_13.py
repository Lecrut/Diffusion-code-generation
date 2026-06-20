def is_negative(number):
    return number < 0

if __name__ == '__main__':
    sample_number = -15
    result = is_negative(sample_number)
    print(f"The sample number is: {sample_number}")
    print(f"Is the sample number negative? {result}")

    another_sample_number = 42
    another_result = is_negative(another_sample_number)
    print(f"The another sample number is: {another_sample_number}")
    print(f"Is the another sample number negative? {another_result}")