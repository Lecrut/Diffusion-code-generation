class GCDCalculator:
    def calculate_gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

if __name__ == '__main__':
    calculator = GCDCalculator()
    print(calculator.calculate_gcd(48, 18))