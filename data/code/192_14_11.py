from typing import List

def find_common_elements(list1: List[str], list2: List[str]) -> List[str]:
    return sorted(set(list1).intersection(list2))

if __name__ == '__main__':
    sample_list1 = ["Apple", "Banana", "Cherry", "Date"]
    sample_list2 = ["apple", "Elderberry", "Banana", "Fig"]
    common_items = find_common_elements(sample_list1, sample_list2)
    print(common_items)