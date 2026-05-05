class DifferenceCalculator:
    def calculate_differences(self, list1, list2):
        if len(list1) != len(list2):
            raise ValueError("Lists must have the same length")
        differences = []
        for i in range(len(list1)):
            differences.append(list1[i] - list2[i])
        return differences
if __name__ == '__main__':
    calculator = DifferenceCalculator()
    list_a = [10, 20, 30, 40]
    list_b = [7, 15, 25, 35]
    result = calculator.calculate_differences(list_a, list_b)
    print(result)