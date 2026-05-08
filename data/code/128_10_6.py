def check_negativity(number):
    if number < 0:
        print(f"The number {number} is negative.")
    else:
        print(f"The number {number} is not negative.")
if __name__ == '__main__':
    sample_number_1 = -15
    sample_number_2 = 42
    sample_number_3 = 0
    sample_number_4 = -1
    check_negativity(sample_number_1)
    check_negativity(sample_number_2)
    check_negativity(sample_number_3)
    check_negativity(sample_number_4)