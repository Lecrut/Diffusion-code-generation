class ListIntersector:
    @staticmethod
    def intersect(*lists):
        sets = [set(lst) for lst in lists]
        common_elements = set.intersection(*sets)
        return list(common_elements)

if __name__ == '__main__':
    intersector = ListIntersector()
    sample_lists = [
        [1, 2, 3, 4],
        [3, 4, 5, 6],
        [4, 5, 7, 8]
    ]
    result = intersector.intersect(*sample_lists)
    print(result)