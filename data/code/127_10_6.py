def is_odd(number):
    return number & 1 == 1

if __name__ == '__main__':
    sample_numbers = [3, 4, 7, 8, 10]
    for num in sample_numbers:
        print(is_odd(num))