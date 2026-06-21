class ListIntersector:
    def __init__(self, list1, list2):
        self.set1 = set(list1)
        self.set2 = set(list2)

    def intersect(self):
        return self.set1.intersection(self.set2)

if __name__ == '__main__':
    intersector = ListIntersector([1, 2, 3, 4, 5], [4, 5, 6, 7, 8])
    intersection_result = intersector.intersect()
    print(intersection_result)