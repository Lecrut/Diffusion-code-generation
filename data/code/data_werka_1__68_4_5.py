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
    sample_list1 = [10, 20, 30, 40]
    sample_list2 = [5, 10, 15, 20]
    calculator = DifferenceCalculator(sample_list1, sample_list2)
    result = calculator.calculate_differences()
    print(result)