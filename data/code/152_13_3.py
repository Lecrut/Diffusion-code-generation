class ListUtils:
    @staticmethod
    def get_intersection(list1, list2):
        set1 = set(list1)
        set2 = set(list2)
        if len(set1) < len(set2):
            smaller_set = set1
            larger_set = set2
        else:
            smaller_set = set2
            larger_set = set1
        intersection = set()
        for item in smaller_set:
            if item in larger_set:
                intersection.add(item)
        return list(intersection)
if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5]
    list_b = [4, 5, 6, 7, 8]
    result1 = ListUtils.get_intersection(list_a, list_b)
    print(f"Intersection of {list_a} and {list_b}: {result1}")
    list_c = [10, 20, 30]
    list_d = [30, 40, 50]
    result2 = ListUtils.get_intersection(list_c, list_d)
    print(f"Intersection of {list_c} and {list_d}: {result2}")
    list_e = ['a', 'b', 'c', 'd']
    list_f = ['c', 'd', 'e', 'f']
    result3 = ListUtils.get_intersection(list_e, list_f)
    print(f"Intersection of {list_e} and {list_f}: {result3}")