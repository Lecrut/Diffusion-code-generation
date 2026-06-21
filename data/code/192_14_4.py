from typing import List

def find_common_elements(list1: List[str], list2: List[str]) -> List[str]:
    if not all((isinstance(item, str) for item in list1 + list2)):
        raise ValueError('Both inputs must be lists of strings.')
    set1 = {item.lower() for item in list1}
    set2 = {item.lower() for item in list2}
    common = sorted(set1 & set2)
    return common
if __name__ == '__main__':
    sample_list_a = ['Apple', 'Banana', 'Cherry', 'Date']
    sample_list_b = ['apple', 'Elderberry', 'Banana', 'Fig']
    try:
        common_items = find_common_elements(sample_list_a, sample_list_b)
        print(common_items)
    except ValueError as e:
        print(e)