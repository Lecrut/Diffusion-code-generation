class ListComparator:
    def get_intersection(self, list1, list2):
        set1 = set(list1)
        set2 = set(list2)
        intersection = set1.intersection(set2)
        return list(intersection)
if __name__ == '__main__':
    comparator = ListComparator()
    list_a = [1, 2, 3, 4, 5]
    list_b = [4, 5, 6, 7, 8]
    result1 = comparator.get_intersection(list_a, list_b)
    print(f"Intersection of {list_a} and {list_b}: {result1}")
    list_c = ['apple', 'banana', 'cherry']
    list_d = ['banana', 'date', 'apple']
    result2 = comparator.get_intersection(list_c, list_d)
    print(f"Intersection of {list_c} and {list_d}: {result2}")
    list_e = [10, 20, 30]
    list_f = [40, 50, 60]
    result3 = comparator.get_intersection(list_e, list_f)
    print(f"Intersection of {list_e} and {list_f}: {result3}")