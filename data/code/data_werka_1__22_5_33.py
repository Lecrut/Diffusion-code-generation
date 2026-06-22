def is_odd_or_even(number):
    remainder = number % 2
    if remainder == 0:
        return 'Even'
    else:
        return 'Odd'
if __name__ == '__main__':
    print(is_odd_or_even(4))
    print(is_odd_or_even(7))