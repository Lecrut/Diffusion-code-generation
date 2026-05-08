class ListUtils:
    @staticmethod
    def get_intersection(list1, list2):
        if len(list1) < len(list2):
            set1 = set(list1)
            set2 = set(list2)
            return list(set1.intersection(set2))
        else:
            set1 = set(list1)
            set2 = set(list2)
            return list(set1.intersection(set2))
if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5]
    list_b = [4, 5, 6, 7, 8]
    result1 = ListUtils.get_intersection(list_a, list_b)
    print(f"Intersection of {list_a} and {list_b}: {result1}")
    list_c = [10, 20, 30]
    list_d = [30, 40, 50]
    result2 = ListUtils.get_intersection(list_c, list_d)
    print(f"Intersection of {list_c} and {list_d}: {result2}")
    list_e = [1, 2, 3]
    list_f = [3, 2, 1]
    result3 = ListUtils.get_intersection(list_e, list_f)
    print(f"Intersection of {list_e} and {list_f}: {result3}")