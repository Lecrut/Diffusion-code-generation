class ElementComparator:
    def compare_elements_at_indices(self, list1, list2, indices):
        return [list1[i] == list2[i] if 0 <= i < len(list1) and 0 <= i < len(list2) else False for i in indices]

if __name__ == '__main__':
    comparator = ElementComparator()
    result1 = comparator.compare_elements_at_indices([1, 2, 3], [4, 5, 6], [0, 2])
    result2 = comparator.compare_elements_at_indices(['a', 'b'], ['c', 'd', 'e'], [1, 2])
    print(result1)
    print(result2)