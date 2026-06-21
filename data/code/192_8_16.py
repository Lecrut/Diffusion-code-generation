from collections import Counter

def validate_lists(list1, list2):
    if not all(isinstance(item, (int, float)) for item in list1 + list2):
        raise ValueError("Both lists must contain only integers or floats")
    return True

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