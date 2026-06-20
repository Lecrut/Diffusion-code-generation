class ListComparator:
    @staticmethod
    def find_longer_list(list1, list2):
        size1 = len(list1)
        size2 = len(list2)
        if size1 > size2:
            return list1
        elif size2 > size1:
            return list2
        else:
            return None

if __name__ == '__main__':
    comparator = ListComparator()
    l1 = [1, 2, 3, 4]
    l2 = [5, 6]
    longer_list = comparator.find_longer_list(l1, l2)
    print(longer_list)