def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

if __name__ == '__main__':
    sample_values = [123, 456, 999, 7, 1001]
    for value in sample_values:
        print(sum_of_digits(value))