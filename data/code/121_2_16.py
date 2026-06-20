class ListLengthComparator:

    def get_longer_list(self, list1, list2):
        size1 = len(list1)
        size2 = len(list2)
        if size1 > size2:
            return list1
        elif size2 > size1:
            return list2
        else:
            return None
if __name__ == '__main__':
    comparator = ListLengthComparator()
    l1 = [1, 2, 3, 4]
    l2 = [5, 6]
    l3 = [7, 8, 9, 10]
    l4 = [11, 12]
    print(comparator.get_longer_list(l1, l2))
    print(comparator.get_longer_list(l2, l3))
    print(comparator.get_longer_list(l3, l4))