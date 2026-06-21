class ListIntersector:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2
        self.set2 = set(list2)

    def find_intersection_ordered(self):
        intersection = []
        for item in self.list1:
            if item in self.set2 and item not in intersection:
                intersection.append(item)
        return intersection

if __name__ == '__main__':
    intersector = ListIntersector([1, 2, 2, 3, 4, 4], [2, 4, 4, 5, 6, 1])
    result = intersector.find_intersection_ordered()
    print(result)