from typing import List

class ListComparator:
    @staticmethod
    def are_lists_equal(list1: List, list2: List) -> bool:
        return list1 == list2

if __name__ == '__main__':
    print(ListComparator.are_lists_equal([1, 2, 3], [1, 2, 3]))
    print(ListComparator.are_lists_equal([1, 2, 3], [3, 2, 1]))
    print(ListComparator.are_lists_equal([], []))
    print(ListComparator.are_lists_equal(['a', 'b'], ['a', 'b']))