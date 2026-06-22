def check_prime(value):
    if value < 2:
        return False
    if value == 2:
        return True
    if value % 2 == 0:
        return False
    limit = int(value**0.5) + 1
    divisor = 3
    while divisor < limit:
        if value % divisor == 0:
            return False
        divisor += 2
    return True

if __name__ == '__main__':
    print(check_prime(2))
    print(check_prime(17))
    print(check_prime(18))
    print(check_prime(97))
    print(check_prime(0))