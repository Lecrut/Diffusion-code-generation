class DifferenceGenerator:
    def __init__(self, list1, list2):
        if len(list1) != len(list2):
            raise ValueError("Both lists must have the same length.")
        self.list1 = list1
        self.list2 = list2

    def generate_differences(self):
        return (abs(num1 - num2) for num1, num2 in zip(self.list1, self.list2))

if __name__ == '__main__':
    data1 = [8, 16, 24, 32]
    data2 = [2, 4, 6, 8]
    
    diff_gen = DifferenceGenerator(data1, data2)
    differences = list(diff_gen.generate_differences())
    
    print("Differences:", differences)