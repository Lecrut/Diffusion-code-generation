def check_negativity(number):
    if number < 0:
        print(f"{number} is negative.")
    else:
        print(f"{number} is not negative.")
if __name__ == '__main__':
    sample_number = -15
    check_negativity(sample_number)
    sample_number_positive = 42
    check_negativity(sample_number_positive)
    sample_number_zero = 0
    check_negativity(sample_number_zero)