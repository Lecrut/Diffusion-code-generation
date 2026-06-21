class FloatingPointComparer:
    TOLERANCE = 1e-9

    @staticmethod
    def compare_elements(list_a, list_b):
        return [x for x in list_a if any(abs(x - y) < FloatingPointComparer.TOLERANCE for y in list_b)]

if __name__ == '__main__':
    sample_list1 = [0.1 + 0.2, 0.3, 0.4]
    sample_list2 = [0.3000000001, 0.5, 0.6]
    comparer = FloatingPointComparer()
    common_elements = comparer.compare_elements(sample_list1, sample_list2)
    print(common_elements)