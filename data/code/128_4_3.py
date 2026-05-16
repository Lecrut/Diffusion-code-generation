def check_and_print_negative(number):
    if number < 0:
        print(f"The number {number} is negative.")
    else:
        print(f"The number {number} is not negative.")
if __name__ == '__main__':
    check_and_print_negative(10)
    check_and_print_negative(-5)
    check_and_print_negative(0)
    check_and_print_negative(3.14)
    check_and_print_negative(-100)