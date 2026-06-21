from typing import List

class Intersector:
    @staticmethod
    def intersect(list1: List[int], list2: List[int]) -> List[int]:
        set1 = set(list1)
        set2 = set(list2)
        return list(set1.intersection(set2))

if __name__ == '__main__':
    intersector = Intersector()
    list1 = [1, 2, 3, 4, 5]
    list2 = [3, 4, 5, 6, 7]
    intersection_result = intersector.intersect(list1, list2)
    print(f"Intersection of {list1} and {list2}: {intersection_result}")