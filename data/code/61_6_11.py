def is_prime(number: int) -> bool:
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    limit = int(number**0.5) + 1
    for i in range(3, limit, 2):
        if number % i == 0:
            return False
    return True

if __name__ == '__main__':
    print(is_prime(2))
    print(is_prime(3))
    print(is_prime(4))
    print(is_prime(17))
    print(is_prime(18))
    print(is_prime(97))
    print(is_prime(1))
    print(is_prime(0))
    print(is_prime(-5))