class ListComparator:
    @staticmethod
    def compare(list_a, list_b):
        set_a = set(list_a)
        set_b = set(list_b)
        return set_a == set_b

if __name__ == '__main__':
    comparator = ListComparator()
    list1 = [1, 2, 3, 4]
    list2 = [1, 2, 5, 4]
    list3 = [1, 2, 3, 4]
    result1 = comparator.compare(list1, list2)
    print(f"Comparing {list1} and {list2}: Equality={result1}")
    result2 = comparator.compare(list1, list3)
    print(f"Comparing {list1} and {list3}: Equality={result2}")