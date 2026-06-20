class ListOperations:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def find_intersection(self):
        return list(set(self.list1) & set(self.list2))

    def find_union(self):
        return list(set(self.list1) | set(self.list2))

    def find_difference(self):
        return list(set(self.list1) - set(self.list2))

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [4, 5, 6, 7, 8]

    operations = ListOperations(sample_list1, sample_list2)

    print("Intersection:", operations.find_intersection())
    print("Union:", operations.find_union())
    print("Difference (list1 - list2):", operations.find_difference())