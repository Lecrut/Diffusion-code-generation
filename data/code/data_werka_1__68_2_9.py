class DifferenceCalculator:
    def calculate_differences(self, list1, list2):
        if len(list1) != len(list2):
            raise ValueError("Lists must have the same length")
        differences = []
        for i in range(len(list1)):
            diff = list1[i] - list2[i]
            differences.append(diff)
        return differences

if __name__ == '__main__':
    calculator = DifferenceCalculator()
    LIST_A = [10, 20, 30, 40]
    LIST_B = [7, 15, 25, 35]
    try:
        result = calculator.calculate_differences(LIST_A, LIST_B)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")