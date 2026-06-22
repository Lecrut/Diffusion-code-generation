class AbsoluteDifferenceGenerator:
    def __init__(self, list1, list2):
        if not (isinstance(list1, list) and isinstance(list2, list)):
            raise ValueError("Both inputs must be lists.")
        if len(list1) != len(list2):
            raise ValueError("Both lists must have the same length.")
        self.list1 = list1
        self.list2 = list2

    def generate_differences(self):
        for num1, num2 in zip(self.list1, self.list2):
            yield abs(num1 - num2)

if __name__ == '__main__':
    try:
        sample_list1 = [8, 16, 24, 32]
        sample_list2 = [4, 8, 12, 16]
        generator = AbsoluteDifferenceGenerator(sample_list1, sample_list2)
        
        print("Absolute Differences:")
        for diff in generator.generate_differences():
            print(diff)
    except ValueError as e:
        print(e)