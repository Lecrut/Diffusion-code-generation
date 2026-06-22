def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

if __name__ == '__main__':
    print(sum_of_digits(123))
    print(sum_of_digits(987654321))
    print(sum_of_digits(0))