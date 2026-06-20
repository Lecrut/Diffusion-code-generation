import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True
if __name__ == '__main__':
    print(is_prime(6))
    print(is_prime(101))
    print(is_prime(11))
    print(is_prime(13441))
    print(is_prime(61))
    print(is_prime(4))
    print(is_prime(1))