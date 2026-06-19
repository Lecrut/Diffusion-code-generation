class DifferenceCalculator:
    def __init__(self):
        self.ERROR_MESSAGE = "Lists must have the same length"

    def calculate_differences(self, list1, list2):
        if len(list1) != len(list2):
            raise ValueError(self.ERROR_MESSAGE)
        differences = []
        for i in range(len(list1)):
            diff = list1[i] - list2[i]
            differences.append(diff)
        return differences

if __name__ == '__main__':
    calculator = DifferenceCalculator()
    list_a = [5, 10, 15, 20]
    list_b = [3, 8, 12, 18]
    try:
        result = calculator.calculate_differences(list_a, list_b)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")