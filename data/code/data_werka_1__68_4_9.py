class DifferenceCalculator:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def calculate_differences(self):
        differences = {}
        for i in range(min(len(self.list1), len(self.list2))):
            differences[i] = self.list1[i] - self.list2[i]
        return differences

if __name__ == '__main__':
    sample_list1 = [7, 14, 21, 28]
    sample_list2 = [1, 3, 5, 7]
    calculator = DifferenceCalculator(sample_list1, sample_list2)
    result_differences = calculator.calculate_differences()
    print(result_differences)

    another_sample_list1 = [100, 200, 300]
    another_sample_list2 = [10, 20, 30]
    another_calculator = DifferenceCalculator(another_sample_list1, another_sample_list2)
    another_result_differences = another_calculator.calculate_differences()
    print(another_result_differences)