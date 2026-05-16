def check_odd_even(number):
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")
if __name__ == '__main__':
    sample_number = 17
    check_odd_even(sample_number)
    sample_number = 24
    check_odd_even(sample_number)
    sample_number = 0
    check_odd_even(sample_number)