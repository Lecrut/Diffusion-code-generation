class PrimeChecker:
    def __init__(self):
        self._primes_cache = {}

    def is_prime(self, n):
        if n in self._primes_cache:
            return self._primes_cache[n]
        result = self._check_primality(n)
        self._primes_cache[n] = result
        return result

    def _check_primality(self, n):
        if n < 2:
            return False
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        limit = int(n**0.5) + 1
        while i <= limit:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def check_multiple(self, numbers):
        results = []
        for num in numbers:
            results.append((num, self.is_prime(num)))
        return results

if __name__ == '__main__':
    checker = PrimeChecker()
    samples = [2, 17, 18, 97, 100, 101, 2003, 2005, 1, 0, -5]
    batch_result = checker.check_multiple(samples)
    for val, is_p in batch_result:
        print(f"{val}: {is_p}")
    print(checker.is_prime(7919))
    print(checker.is_prime(7920))