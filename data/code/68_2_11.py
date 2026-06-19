class DifferenceCalculator:
    def calculate_differences(self, list1, list2):
        return [abs(a - b) for a, b in zip(list1, list2)]

if __name__ == '__main__':
    calc = DifferenceCalculator()
    list1 = [10, 20, 30, 40]
    list2 = [1, 2, 3, 4]
    differences = calc.calculate_differences(list1, list2)
    print(differences)