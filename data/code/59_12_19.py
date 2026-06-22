def sum_of_digits(n):
    if n < 0:
        n = -n
    if n < 10:
        return n
    return n % 10 + sum_of_digits(n // 10)

if __name__ == '__main__':
    result = sum_of_digits(12345)
    print(result)
    result = sum_of_digits(9876)
    print(result)
    result = sum_of_digits(0)
    print(result)
    result = sum_of_digits(-42)
    print(result)