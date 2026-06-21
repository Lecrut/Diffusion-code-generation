class ListIntersector:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def find_common_elements_ordered(self):
        set2 = set(self.list2)
        return [item for item in self.list1 if item in set2]

if __name__ == '__main__':
    intersector = ListIntersector([1, 2, 2, 3, 4, 4], [2, 4, 4, 5, 6, 1])
    result = intersector.find_common_elements_ordered()
    print(result)