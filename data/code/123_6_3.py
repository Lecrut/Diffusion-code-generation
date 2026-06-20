def sum_of_digits(n):
    if not isinstance(n, int):
        raise ValueError("Input must be an integer.")
    return sum(int(digit) for digit in str(abs(n)))

if __name__ == '__main__':
    print(sum_of_digits(12345))
    print(sum_of_digits(-9876))