import math

def is_prime(n: int) -> bool:
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

def main():
    samples = [2, 3, 4, 17, 18, 25, 29, 30, 31, 37, 49, 97, 100, 101]
    for num in samples:
        print(f"{num}: {is_prime(num)}")

if __name__ == '__main__':
    main()