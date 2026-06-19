class DifferenceCalculator:
    def __init__(self):
        self.difference_map = {}

    def calculate_differences(self, list1, list2):
        if len(list1) != len(list2):
            raise ValueError("Lists must have the same length")
        
        differences = []
        for i in range(len(list1)):
            diff = list1[i] - list2[i]
            differences.append(diff)
            self.difference_map[i] = diff
        
        return differences

if __name__ == '__main__':
    calculator = DifferenceCalculator()
    list_a = [5, 15, 25, 35]
    list_b = [2, 10, 18, 26]
    
    try:
        result = calculator.calculate_differences(list_a, list_b)
        print("Differences:", result)
        print("Difference Map:", calculator.difference_map)
    except ValueError as e:
        print(f"Error: {e}")