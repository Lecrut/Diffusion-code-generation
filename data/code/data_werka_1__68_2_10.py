class DifferenceCalculator:
    def calculate_differences(self, list1, list2):
        if len(list1) != len(list2):
            raise ValueError("Lists must have the same length")
        
        differences = []
        for index in range(len(list1)):
            diff = self.compute_difference(list1[index], list2[index])
            differences.append(diff)
        
        return differences

    def compute_difference(self, a, b):
        return a - b

if __name__ == '__main__':
    calculator = DifferenceCalculator()
    sample_list1 = [50, 60, 70, 80]
    sample_list2 = [40, 50, 60, 70]
    
    try:
        result = calculator.calculate_differences(sample_list1, sample_list2)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")