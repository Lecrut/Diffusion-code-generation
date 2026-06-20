def is_odd(number):
    return number & 1 == 1
if __name__ == '__main__':
    sample_numbers = [10, 7, 0, -4, 15]
    for num in sample_numbers:
        print(f'Number: {num}, Is Odd: {is_odd(num)}')