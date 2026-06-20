ODD_CHECK_DIVISOR = 2

def is_odd(number):
    return number % ODD_CHECK_DIVISOR == 1
if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for num in sample_numbers:
        print(f'{num} is {('Odd' if is_odd(num) else 'Even')}')