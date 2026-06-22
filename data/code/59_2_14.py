def sum_of_digits(n):
    if n < 10:
        return n
    return (n % 10) + sum_of_digits(n // 10)

if __name__ == '__main__':
    number = 12345
    result = sum_of_digits(number)
    print(result)
    number = 0
    result = sum_of_digits(number)
    print(result)
    number = 99999
    result = sum_of_digits(number)
    print(result)