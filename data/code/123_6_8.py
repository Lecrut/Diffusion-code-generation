def sum_of_digits(n):
    return sum(int(digit) for digit in str(abs(n)))

if __name__ == '__main__':
    sample_number = 56789
    result = sum_of_digits(sample_number)
    print(result)