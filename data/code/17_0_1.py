def check_even_or_odd(number):
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")
if __name__ == '__main__':
    sample_number = 17
    check_even_or_odd(sample_number)
    sample_number = 42
    check_even_or_odd(sample_number)
    sample_number = 0
    check_even_or_odd(sample_number)