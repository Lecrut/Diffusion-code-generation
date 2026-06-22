class ListComparator:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def are_identical(self):
        if len(self.list1) != len(self.list2):
            return False
        for elem1, elem2 in zip(self.list1, self.list2):
            if elem1 != elem2:
                return False
        return True

if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5]
    list_b = [1, 2, 3, 4, 5]
    list_c = [1, 2, 3, 4, 6]

    comparator_ab = ListComparator(list_a, list_b)
    comparator_ac = ListComparator(list_a, list_c)

    print(comparator_ab.are_identical())
    print(comparator_ac.are_identical())