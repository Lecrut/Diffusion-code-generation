class ListIntersector:
    @staticmethod
    def to_set(lst):
        return set(lst)

    @staticmethod
    def intersect_sets(*sets):
        return set.intersection(*sets)

    @classmethod
    def find_common_elements(cls, *lists):
        sets = [cls.to_set(lst) for lst in lists]
        common_elements = cls.intersect_sets(*sets)
        return list(common_elements)

if __name__ == '__main__':
    intersector = ListIntersector()
    list_a = [1, 2, 3, 4, 5]
    list_b = [4, 5, 6, 7, 8]
    result = intersector.find_common_elements(list_a, list_b)
    print(result)