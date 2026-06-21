from collections import Counter

def validate_lists(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise ValueError("Both inputs must be lists.")
    
    for item in list1 + list2:
        if not isinstance(item, (int, str)):
            raise ValueError("List elements must be integers or strings.")

def count_common_elements(list1, list2):
    validate_lists(list1, list2)
    counter1 = Counter(list1)
    counter2 = Counter(list2)
    common_elements = counter1 & counter2
    return sum(common_elements.values())

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5, 5]
    sample_list2 = [4, 5, 5, 6, 7]
    print(count_common_elements(sample_list1, sample_list2))