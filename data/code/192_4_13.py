class FloatingPointComparator:
    TOLERANCE = 1e-9

    @staticmethod
    def are_close(value1, value2):
        return abs(value1 - value2) < FloatingPointComparator.TOLERANCE

    @staticmethod
    def find_common_elements(list_a, list_b):
        common_elements = []
        for item in list_a:
            if any(FloatingPointComparator.are_close(item, elem) for elem in list_b):
                common_elements.append(item)
        return common_elements

if __name__ == '__main__':
    sample_list1 = [0.1 + 0.2, 0.3, 0.4]
    sample_list2 = [0.3000000001, 0.5, 0.6]
    comparator = FloatingPointComparator()
    common_elements = comparator.find_common_elements(sample_list1, sample_list2)
    print(common_elements)