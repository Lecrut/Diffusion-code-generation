class DifferenceCalculator:
    def calculate_differences(self, list1, list2):
        if len(list1) != len(list2):
            raise ValueError("Lists must have the same length")
        return [a - b for a, b in zip(list1, list2)]

if __name__ == '__main__':
    calculator = DifferenceCalculator()
    list_a = [10, 20, 30, 40]
    list_b = [7, 15, 25, 35]
    try:
        result1 = calculator.calculate_differences(list_a, list_b)
        print("Differences between list_a and list_b:", result1)
        
        list_c = [5, 10, 15, 20]
        list_d = [3, 8, 12, 18]
        result2 = calculator.calculate_differences(list_c, list_d)
        print("Differences between list_c and list_d:", result2)
    except ValueError as e:
        print(f"Error: {e}")