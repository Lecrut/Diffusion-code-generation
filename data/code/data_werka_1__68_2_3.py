class DifferenceCalculator:
    def calculate_differences(self, list1, list2):
        return [abs(a - b) for a, b in zip(list1, list2)]

if __name__ == '__main__':
    calc = DifferenceCalculator()
    list1 = [5, 10, 15, 20]
    list2 = [3, 8, 12, 18]
    differences = calc.calculate_differences(list1, list2)
    print(differences)