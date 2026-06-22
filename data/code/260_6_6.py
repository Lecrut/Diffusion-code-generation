class ListComparer:
    TOLERANCE = 1e-09

    @staticmethod
    def are_elements_equal(value1, value2):
        return abs(value1 - value2) < ListComparer.TOLERANCE

    @classmethod
    def find_matching_indices(cls, list1, list2):
        matching_indices = []
        for index, (value1, value2) in enumerate(zip(list1, list2)):
            if cls.are_elements_equal(value1, value2):
                matching_indices.append(index)
        return matching_indices

if __name__ == '__main__':
    sample_list1 = [1.0, 2.5, 3.0, 4.5]
    sample_list2 = [1.0, 2.6, 3.0, 4.5]
    print(ListComparer.find_matching_indices(sample_list1, sample_list2))