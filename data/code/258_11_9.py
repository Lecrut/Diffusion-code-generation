class AverageCalculator:
    @staticmethod
    def calculate_averages(list1, list2):
        return [(a + b) / 2 for a, b in zip(list1, list2)]

if __name__ == '__main__':
    calculator = AverageCalculator()
    sample_list1 = [10, 20, 30]
    sample_list2 = [5, 15, 25]
    result = calculator.calculate_averages(sample_list1, sample_list2)
    print(result)