from typing import List

def find_common_elements(list1: List[str], list2: List[str]) -> List[str]:
    if not all(isinstance(item, str) for item in list1 + list2):
        raise ValueError("Both lists must contain only strings.")
    
    set1 = set(list1)
    set2 = set(list2)
    common = set1.intersection(set2)
    return sorted(common)

if __name__ == '__main__':
    list_a = ["Apple", "Banana", "Cherry", "Date"]
    list_b = ["apple", "Elderberry", "Banana", "Fig"]
    common_items = find_common_elements(list_a, list_b)
    print(common_items)