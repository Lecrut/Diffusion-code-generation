class ElementDifferencesCalculator:
    @staticmethod
    def calculate_difference(a, b):
        return abs(a - b)

    @classmethod
    def find_element_differences(cls, list1, list2):
        if len(list1) != len(list2):
            raise ValueError("Both lists must have the same length.")
        differences = []
        for a, b in zip(list1, list2):
            differences.append(cls.calculate_difference(a, b))
        return differences

if __name__ == '__main__':
    sample_list1 = [7, 14, 21, 28]
    sample_list2 = [3, 9, 15, 21]
    try:
        result = ElementDifferencesCalculator.find_element_differences(sample_list1, sample_list2)
        print(result)
    except ValueError as e:
        print(e)