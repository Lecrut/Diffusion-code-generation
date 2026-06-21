from typing import List

class IntersectionFinder:
    def find_common_elements(self, list1: List[int], list2: List[int]) -> List[int]:
        set1 = set(list1)
        set2 = set(list2)
        return list(set1.intersection(set2))

if __name__ == '__main__':
    finder = IntersectionFinder()
    list1 = [1, 2, 3, 4, 5]
    list2 = [3, 4, 5, 6, 7]
    common_elements = finder.find_common_elements(list1, list2)
    print(f"Common elements in {list1} and {list2}: {common_elements}")