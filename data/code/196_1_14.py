from typing import List

class ListMerger:
    def __init__(self, list1: List[int], list2: List[int]):
        self.list1 = list1
        self.list2 = list2

    def merge(self) -> List[int]:
        return [item for sublist in (self.list1, self.list2) for item in sublist]

if __name__ == '__main__':
    merger_instance = ListMerger([1, 2, 3], [4, 5, 6])
    merged_list = merger_instance.merge()
    print(merged_list)