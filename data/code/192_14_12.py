from typing import List

def find_common_elements(list1: List[str], list2: List[str]) -> List[str]:
    if not all(isinstance(item, str) for item in list1 + list2):
        raise ValueError("Both inputs must be lists of strings.")
    set1 = set(list1)
    set2 = set(list2)
    common = set1.intersection(set2)
    return sorted(common)

if __name__ == '__main__':
    sample_list1 = ["Apple", "Banana", "Cherry", "Date"]
    sample_list2 = ["apple", "Elderberry", "Banana", "Fig"]
    try:
        common_items = find_common_elements(sample_list1, sample_list2)
        print(common_items)
    except ValueError as e:
        print(e)