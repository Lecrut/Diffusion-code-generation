def sum_of_digits(n):
    if n < 10:
        return n
    last_digit = n % 10
    remaining = n // 10
    return last_digit + sum_of_digits(remaining)

if __name__ == '__main__':
    print(sum_of_digits(12345))
    print(sum_of_digits(9876543210))
    print(sum_of_digits(0))
    print(sum_of_digits(7))