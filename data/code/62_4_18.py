class DivisorCalculator:
    TARGET = 60

    @staticmethod
    def compute_divisors(number):
        small = []
        large = []
        limit = int(number ** 0.5)
        for candidate in range(1, limit + 1):
            if number % candidate == 0:
                small.append(candidate)
                complement = number // candidate
                if complement != candidate:
                    large.append(complement)
        return small + large[::-1]

    def get_target_divisors(self):
        return self.compute_divisors(self.TARGET)

if __name__ == '__main__':
    calculator = DivisorCalculator()
    print(calculator.get_target_divisors())