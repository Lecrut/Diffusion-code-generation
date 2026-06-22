def sum_digits(number):
    return sum(int(digit) for digit in str(abs(number)))

if __name__ == '__main__':
    sample_values = [123, 9876543210, 0, -456]
    for value in sample_values:
        print(sum_digits(value))