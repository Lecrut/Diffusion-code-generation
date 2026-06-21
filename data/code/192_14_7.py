from typing import List

def find_common_elements(list1: List[str], list2: List[str]) -> List[str]:
    set1 = set(item.lower() for item in list1)
    set2 = set(item.lower() for item in list2)
    common = set1.intersection(set2)
    return sorted([item.capitalize() for item in common])

if __name__ == '__main__':
    sample_list_a = ["Apple", "Banana", "Cherry", "Date"]
    sample_list_b = ["apple", "Fig", "Banana", "Grape"]
    common_items = find_common_elements(sample_list_a, sample_list_b)
    print(common_items)