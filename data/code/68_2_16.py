class DifferenceCalculator:
    def calculate_differences(self, list1, list2):
        if len(list1) != len(list2):
            raise ValueError("Lists must have the same length")
        return [a - b for a, b in zip(list1, list2)]

if __name__ == '__main__':
    calculator = DifferenceCalculator()
    list_a = [50, 60, 70, 80]
    list_b = [40, 55, 70, 90]
    try:
        result = calculator.calculate_differences(list_a, list_b)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")