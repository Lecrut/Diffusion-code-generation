def sum_digits(n):
    total = 0
    while n > 0:
        digit = n % 10
        total = total + digit
        n = n // 10
    return total

if __name__ == '__main__':
    number1 = 12345
    number2 = 9876543210
    number3 = 0
    print(sum_digits(number1))
    print(sum_digits(number2))
    print(sum_digits(number3))