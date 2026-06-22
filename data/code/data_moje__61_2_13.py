class PrimeChecker:
    TWO = 2
    THREE = 3
    SIX = 6

    @staticmethod
    def is_prime(n):
        if n < PrimeChecker.TWO:
            return False
        if n == PrimeChecker.TWO or n == PrimeChecker.THREE:
            return True
        if n % PrimeChecker.TWO == 0 or n % PrimeChecker.THREE == 0:
            return False
        i = PrimeChecker.THREE
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += PrimeChecker.SIX
        return True

if __name__ == '__main__':
    sample_inputs = [-5, 0, 1, 2, 3, 4, 5, 10, 17, 25, 97, 100, 997, 1000]
    results = [PrimeChecker.is_prime(x) for x in sample_inputs]
    print(results)