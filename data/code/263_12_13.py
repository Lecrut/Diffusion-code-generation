class ListComparator:
    def compare(self, list1, list2):
        return [element for element in set(list1) if element in set(list2)]

if __name__ == '__main__':
    comparator = ListComparator()
    print(comparator.compare([1, 2, 3, 4], [3, 4, 5, 6]))
    print(comparator.compare(['apple', 'banana'], ['banana', 'cherry']))
    print(comparator.compare([True, False, True], [False, True]))