def check_negativity(number):
    if number < 0:
        return True
    else:
        return False
if __name__ == '__main__':
    sample_number = -15
    is_negative = check_negativity(sample_number)
    print(f"The sample number is: {sample_number}")
    print(f"Is the sample number negative? {is_negative}")