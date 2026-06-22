class DifferenceCalculator:
    @staticmethod
    def compute_difference(a, b):
        return abs(a - b)

if __name__ == '__main__':
    sample_values = [10, 5, 8, 2, 15]
    for i in range(len(sample_values) - 1):
        diff = DifferenceCalculator.compute_difference(sample_values[i], sample_values[i + 1])
        print(diff)