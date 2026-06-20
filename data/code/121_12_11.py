class ListLengthComparator:
    def compare(self, list1, list2):
        len1 = len(list1)
        len2 = len(list2)
        if len1 > len2:
            return list1
        elif len2 > len1:
            return list2
        else:
            return None

if __name__ == '__main__':
    comparator = ListLengthComparator()
    print(comparator.compare([1, 2, 3], [4, 5]))
    print(comparator.compare(['a', 'b'], ['c', 'd', 'e']))
    print(comparator.compare([], []))
    print(comparator.compare([10], [10]))