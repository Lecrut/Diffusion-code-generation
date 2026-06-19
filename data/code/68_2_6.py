class DifferenceCalculator:
    def calculate_differences(self, list1, list2):
        if len(list1) != len(list2):
            raise ValueError("Lists must have the same length")
        differences = []
        for a, b in zip(list1, list2):
            diff = a - b
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