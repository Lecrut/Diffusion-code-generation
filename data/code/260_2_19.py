class SetOperations:

    def find_common_elements(self, set1, set2):
        return set1.intersection(set2)
if __name__ == '__main__':
    set_ops = SetOperations()
    sample_set1 = {1, 2, 3, 4, 5}
    sample_set2 = {4, 5, 6, 7, 8}
    common_elements = set_ops.find_common_elements(sample_set1, sample_set2)
    print(common_elements)
    sample_set3 = {9, 10, 11}
    sample_set4 = {11, 12, 13, 14}
    common_elements = set_ops.find_common_elements(sample_set3, sample_set4)
    print(common_elements)
    empty_set = set()
    full_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    common_elements = set_ops.find_common_elements(empty_set, full_set)
    print(common_elements)