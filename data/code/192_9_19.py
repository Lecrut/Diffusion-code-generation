from typing import List

class SetOperations:
    def __init__(self, *lists: List[int]):
        self.sets = [set(lst) for lst in lists]

    def intersection(self) -> List[int]:
        common_elements = set.intersection(*self.sets)
        return list(common_elements)

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [3, 4, 5, 6, 7]
    list3 = [4, 5, 8, 9, 10]
    set_ops = SetOperations(list1, list2, list3)
    common1 = set_ops.intersection()
    print(f"Common to {list1}, {list2}, and {list3}: {common1}")