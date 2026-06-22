def get_divisors(n):
    if n == 0:
        return []
    if n < 0:
        n = -n
    factors = {}
    limit = int(n**0.5)
    for i in range(1, limit + 1):
        if n % i == 0:
            factors[i] = None
            factors[n // i] = None
    return sorted(factors.keys())

class DivisorCalculator:
    def __init__(self, value):
        self.value = value

    def calculate(self):
        return get_divisors(self.value)

if __name__ == '__main__':
    sample_number = 36
    calculator = DivisorCalculator(sample_number)
    print(calculator.calculate())