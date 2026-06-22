def is_prime(number):
    if type(number) is not int:
        raise TypeError("Input must be an integer")
    if number == 2:
        return True
    if number < 2 or number % 2 == 0:
        return False
    limit = int(number**0.5)
    divisor = 3
    while divisor <= limit:
        if number % divisor == 0:
            return False
        divisor += 2
    return True

if __name__ == '__main__':
    print(is_prime(7919))
    print(is_prime(10))