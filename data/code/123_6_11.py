def digit_sum(n):
    n = abs(n)
    return sum(int(digit) for digit in str(n))

if __name__ == '__main__':
    sample_number = 987654321
    result = digit_sum(sample_number)
    print(result)