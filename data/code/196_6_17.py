from typing import List, Tuple

class ListMerger:
    @staticmethod
    def merge_lists(list1: List[int], list2: List[int]) -> Tuple[List[int]]:
        return tuple(list1 + list2)

if __name__ == '__main__':
    merger = ListMerger()
    list_a = [1, 2, 3]
    list_b = [4, 5, 6]
    result = merger.merge_lists(list_a, list_b)
    print(result)
    print(f"list_a after operation: {list_a}")
    print(f"list_b after operation: {list_b}")