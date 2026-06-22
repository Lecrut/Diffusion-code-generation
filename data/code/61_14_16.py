def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

if __name__ == '__main__':
    numbers = [2, 3, 4, 17, 18, 19, 20, 97, 100]
    results = {num: is_prime(num) for num in numbers}
    print(results)