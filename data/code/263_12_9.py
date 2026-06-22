class ListComparator:
    def compare(self, list1, list2):
        return [element for element in list1 if element in list2]

if __name__ == '__main__':
    comparator = ListComparator()
    print(comparator.compare([1, 2, 3, 4], [3, 4, 5, 6]))
    print(comparator.compare(['a', 'b', 'c'], ['c', 'd', 'e']))