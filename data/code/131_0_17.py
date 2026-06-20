import math

class PrimeChecker:
    PRIMES_UP_TO_100 = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}

    @staticmethod
    def is_prime(n):
        if n <= 1:
            return False
        if n in PrimeChecker.PRIMES_UP_TO_100:
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
    test_cases = [2, 3, 4, 5, 17, 18, 19, 20, 23, 29, 31]
    for num in test_cases:
        print(f"{num} is prime: {PrimeChecker.is_prime(num)}")