def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

if __name__ == '__main__':
    numbers = [2, 3, 4, 17, 25, 7919, 100, 1, 0]
    for num in numbers:
        print(f"{num} is prime: {is_prime(num)}")