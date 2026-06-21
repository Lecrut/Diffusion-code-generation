from typing import List

def validate_lists(list1: List[str], list2: List[str]) -> None:
    if not all(isinstance(item, str) for item in list1 + list2):
        raise ValueError("Both lists must contain only strings.")

def find_common_elements(list1: List[str], list2: List[str]) -> List[str]:
    validate_lists(list1, list2)
    set1 = set(list1.lower())
    set2 = set(list2.lower())
    common = set1.intersection(set2)
    return sorted(common)

if __name__ == '__main__':
    sample_list1 = ["Apple", "Banana", "Cherry", "Date"]
    sample_list2 = ["apple", "Elderberry", "Banana", "Fig"]
    common_items = find_common_elements(sample_list1, sample_list2)
    print(common_items)