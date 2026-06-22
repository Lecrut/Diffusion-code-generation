class ListComparator:
    @staticmethod
    def find_common_elements(list1, list2):
        set1 = set(list1)
        set2 = set(list2)
        return sorted(set1.intersection(set2))

if __name__ == '__main__':
    comparator = ListComparator()
    result = comparator.find_common_elements([1, 2, 2, 3, 4], [2, 1, 4, 3, 2])
    print(f"Common elements: {result}")