class DifferenceCalculator:
    def calculate_differences(self, list1, list2):
        differences = []
        for i in range(min(len(list1), len(list2))):
            differences.append(abs(list1[i] - list2[i]))
        return differences

if __name__ == '__main__':
    calculator = DifferenceCalculator()
    list1 = [5, 10, 15, 20]
    list2 = [3, 8, 12, 18]
    result = calculator.calculate_differences(list1, list2)
    print(result)