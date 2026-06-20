class DifferenceCalculator:
    @staticmethod
    def calculate_difference(a, b):
        return a - b

if __name__ == '__main__':
    result1 = DifferenceCalculator.calculate_difference(10, 5)
    print(f"Difference between 10 and 5: {result1}")