class ListIntersector:
    @staticmethod
    def intersect(*lists):
        return sorted(set.intersection(*map(set, lists)))

if __name__ == '__main__':
    intersector = ListIntersector()
    result = intersector.intersect([1, 2, 3], [2, 3, 4], [3, 4, 5])
    print(result)