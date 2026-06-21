from typing import List

def find_intersection(list1: List[int], list2: List[int]) -> List[int]:
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise ValueError("Both arguments must be lists of integers.")
    
    set1 = set(list1)
    set2 = set(list2)
    
    return list(set1.intersection(set2))

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [3, 4, 5, 6, 7]
    intersection = find_intersection(list1, list2)
    print(f"Common elements in {list1} and {list2}: {intersection}")