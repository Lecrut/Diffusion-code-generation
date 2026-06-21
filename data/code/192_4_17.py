class FloatComparator:
    TOLERANCE = 1e-9

    @staticmethod
    def are_floats_close(a, b):
        return abs(a - b) < FloatComparator.TOLERANCE

    @staticmethod
    def find_common_elements(list_a, list_b):
        common_elements = []
        for item in list_a:
            if any(FloatComparator.are_floats_close(item, y) for y in list_b):
                common_elements.append(item)
        return common_elements

if __name__ == '__main__':
    sample_list1 = [0.1 + 0.2, 0.3, 0.4]
    sample_list2 = [0.3000000001, 0.5, 0.6]
    comparator = FloatComparator()
    result = comparator.find_common_elements(sample_list1, sample_list2)
    print(result)