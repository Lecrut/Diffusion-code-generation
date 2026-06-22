class AbsoluteDifferenceCalculator:
    def __init__(self, list1, list2):
        if len(list1) != len(list2):
            raise ValueError("Both lists must have the same length.")
        self.list1 = list1
        self.list2 = list2

    def calculate_differences(self):
        for num1, num2 in zip(self.list1, self.list2):
            yield abs(num1 - num2)

if __name__ == '__main__':
    calculator = AbsoluteDifferenceCalculator([5, 10, 15, 20], [3, 6, 9, 12])
    for diff in calculator.calculate_differences():
        print(diff)