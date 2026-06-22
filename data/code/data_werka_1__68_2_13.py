class DifferenceCalculator:
    def calculate_differences(self, list1, list2):
        self._validate_lists(list1, list2)
        differences = []
        for i in range(len(list1)):
            diff = self._compute_difference(list1[i], list2[i])
            differences.append(diff)
        return differences

    def _validate_lists(self, list1, list2):
        if len(list1) != len(list2):
            raise ValueError("Lists must have the same length")

    def _compute_difference(self, a, b):
        return a - b

if __name__ == '__main__':
    calculator = DifferenceCalculator()
    list_a = [5, 10, 15, 20]
    list_b = [3, 8, 12, 18]
    try:
        result = calculator.calculate_differences(list_a, list_b)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")