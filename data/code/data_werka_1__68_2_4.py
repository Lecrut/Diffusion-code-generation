class DifferenceCalculator:
    def calculate_differences(self, list1, list2):
        differences = []
        for num1, num2 in zip(list1, list2):
            differences.append(num1 - num2)
        return differences

if __name__ == '__main__':
    calculator = DifferenceCalculator()
    list1 = [5, 10, 15, 20]
    list2 = [3, 6, 9, 12]
    result = calculator.calculate_differences(list1, list2)
    print(result)