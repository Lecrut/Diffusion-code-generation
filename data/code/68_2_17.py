class DifferenceCalculator:
    MAX_LIST_LENGTH = 1000

    @staticmethod
    def validate_lists(list1, list2):
        if len(list1) != len(list2):
            raise ValueError("Lists must have the same length")
        if len(list1) > DifferenceCalculator.MAX_LIST_LENGTH:
            raise ValueError("Lists are too long")

    def calculate_differences(self, list1, list2):
        DifferenceCalculator.validate_lists(list1, list2)
        differences = [a - b for a, b in zip(list1, list2)]
        return differences

if __name__ == '__main__':
    calculator = DifferenceCalculator()
    list_a = [50, 60, 70, 80]
    list_b = [10, 20, 30, 40]
    try:
        result = calculator.calculate_differences(list_a, list_b)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")