from typing import List

def find_common_elements(list1: List[int], list2: List[int]) -> List[int]:
    return [value for value in set(list1) if value in list2]

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [3, 4, 5, 6, 7]
    common_elements = find_common_elements(list1, list2)
    print(f"Common elements in {list1} and {list2}: {common_elements}")