def check_zero(number):
    if number == 0:
        print("The number is zero.")
    else:
        print("The number is not zero.")
if __name__ == '__main__':
    sample_values = [0, 5, -3, 0, 100]
    for value in sample_values:
        check_zero(value)