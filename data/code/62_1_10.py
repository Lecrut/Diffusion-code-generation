class DivisorCalculator:
    def __init__(self, target_number):
        self.target_number = target_number

    def find_positive_divisors(self):
        if self.target_number <= 0:
            return []
        collected_divisors = []
        limit = int(self.target_number ** 0.5)
        for candidate in range(1, limit + 1):
            if self.target_number % candidate == 0:
                collected_divisors.append(candidate)
                paired_divisor = self.target_number // candidate
                if paired_divisor != candidate:
                    collected_divisors.append(paired_divisor)
        return sorted(collected_divisors)

if __name__ == '__main__':
    sample_value = 100
    calculator = DivisorCalculator(sample_value)
    result_list = calculator.find_positive_divisors()
    print(result_list)