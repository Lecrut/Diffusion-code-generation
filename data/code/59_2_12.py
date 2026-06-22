def sum_of_digits(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)

if __name__ == '__main__':
    print(sum_of_digits(0))
    print(sum_of_digits(5))
    print(sum_of_digits(123))
    print(sum_of_digits(9876543210))
    print(sum_of_digits(1000000000))