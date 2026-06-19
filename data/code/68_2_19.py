class DifferenceCalculator:
    def calculate_differences(self, list1, list2):
        if len(list1) != len(list2):
            raise ValueError("Lists must have the same length")
        differences = []
        for idx in range(len(list1)):
            diff = self.compute_difference(list1[idx], list2[idx])
            differences.append(diff)
        return differences

    def compute_difference(self, a, b):
        return a - b

if __name__ == '__main__':
    calc = DifferenceCalculator()
    sample_list1 = [50, 60, 70, 80]
    sample_list2 = [45, 55, 65, 75]
    try:
        diff_result = calc.calculate_differences(sample_list1, sample_list2)
        print(diff_result)
    except ValueError as e:
        print(f"Error: {e}")