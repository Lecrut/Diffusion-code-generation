class LengthCalculator:
    @staticmethod
    def calculate_lengths(a, b):
        if a <= 0 or b <= 0:
            raise ValueError("Lengths must be positive numbers")
        difference = abs(a - b)
        ratio = max(a, b) / min(a, b)
        return {
            'original_lengths': (a, b),
            'difference': difference,
            'ratio': ratio
        }

if __name__ == '__main__':
    length1 = 15
    length2 = 3
    result = LengthCalculator.calculate_lengths(length1, length2)
    print(result)