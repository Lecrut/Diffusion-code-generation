def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

if __name__ == '__main__':
    number = 12345
    result = sum_of_digits(number)
    print(result)