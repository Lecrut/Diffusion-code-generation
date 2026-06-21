class ListIntersector:
    @staticmethod
    def hashable(x):
        try:
            hash(x)
            return True
        except TypeError:
            return False

    @staticmethod
    def intersect(list1, list2):
        set1 = {x for x in list1 if ListIntersector.hashable(x)}
        set2 = {x for x in list2 if ListIntersector.hashable(x)}
        common_elements = set1.intersection(set2)
        return list(common_elements)

if __name__ == '__main__':
    intersector = ListIntersector()
    result = intersector.intersect([1, 2, 3, (4, 5), 'a', {'b': 2}], [3, (4, 5), 'c'])
    print(result)