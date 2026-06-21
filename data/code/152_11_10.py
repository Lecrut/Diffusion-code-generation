class ListIntersector:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.set2 = set(list2)

    def get_common_elements_ordered(self):
        return [item for item in self.list1 if item in self.set2]

if __name__ == '__main__':
    intersector_a = ListIntersector([1, 2, 2, 3, 4, 4], [2, 4, 4, 5, 6, 1])
    intersector_b = ListIntersector([1, 2, 3, 4, 5, 6], [4, 5, 6, 7, 8, 9])
    print(intersector_a.get_common_elements_ordered())
    print(intersector_b.get_common_elements_ordered())