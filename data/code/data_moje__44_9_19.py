class AverageCalculator:
    PREDEFINED_DATA = [5, 15, 25, 35, 45, 55]

    @staticmethod
    def compute(numbers):
        if len(numbers) == 0:
            return 0.0
        running_total = 0
        element_count = 0
        for value in numbers:
            running_total += value
            element_count += 1
        return running_total / element_count

if __name__ == '__main__':
    result = AverageCalculator.compute(AverageCalculator.PREDEFINED_DATA)
    print(result)