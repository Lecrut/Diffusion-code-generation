class IndexComparator:
    EQUAL = True
    NOT_EQUAL = False

    @staticmethod
    def _validate_index(index, length):
        return isinstance(index, int) and 0 <= index < length

    @staticmethod
    def compare_elements_at_indices(list1, list2, indices):
        len1 = len(list1)
        len2 = len(list2)
        results = []
        for idx in indices:
            if IndexComparator._validate_index(idx, len1) and IndexComparator._validate_index(idx, len2):
                results.append(list1[idx] == list2[idx])
            else:
                results.append(IndexComparator.NOT_EQUAL)
        return results

if __name__ == '__main__':
    data_a = [10, 20, 30, 40, 50]
    data_b = [10, 25, 30, 45, 60]
    target_indices = [0, 1, 2, 3, 4, 5, -1]
    comparator = IndexComparator()
    print(comparator.compare_elements_at_indices(data_a, data_b, target_indices))