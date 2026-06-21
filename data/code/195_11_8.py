class ListIntersector:
    def __init__(self, list1):
        self.list1 = list1
        self.set1 = set(list1)

    def intersect(self, list2):
        result = []
        for item in self.list1:
            if item in self.set1 and item not in result:
                result.append(item)
        return result

if __name__ == '__main__':
    intersector = ListIntersector([1, 2, 3, 4, 5, 5, 6])
    print(intersector.intersect([4, 5, 6, 7, 8]))
    print(intersector.intersect([4, 5, 5, 7, 8]))
    print(intersector.intersect([4, 5, 6, 7, 8, 9]))