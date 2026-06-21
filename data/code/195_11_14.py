class ListIntersector:
    @staticmethod
    def intersect_lists(list1, list2):
        set2 = set(list2)
        return [item for item in list1 if item in set2]

if __name__ == '__main__':
    intersector = ListIntersector()
    sample_list1 = [1, 2, 3, 4, 5, 5, 6]
    sample_list2 = [4, 5, 6, 7, 8, 9]
    result = intersector.intersect_lists(sample_list1, sample_list2)
    print(result)