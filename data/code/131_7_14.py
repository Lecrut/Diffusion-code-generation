class GCDCalculator:
    @staticmethod
    def gcd(a: int, b: int) -> int:
        while b != 0:
            a, b = b, a % b
        return a

if __name__ == '__main__':
    calculator = GCDCalculator()
    print(calculator.gcd(48, 18))