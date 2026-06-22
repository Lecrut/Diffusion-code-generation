class SumCalculator:
    NUM_VALUES = 7

    @staticmethod
    def calculate_sum(values):
        return sum(values)

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5, 6, 7]
    result = SumCalculator.calculate_sum(sample_values)
    print(f"Sum of {sample_values}: {result}")