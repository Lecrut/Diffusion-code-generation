def sum_of_digits(n):
    return sum([int(digit) for digit in str(n)])

if __name__ == '__main__':
    number = 12345
    result = sum_of_digits(number)
    print(result)