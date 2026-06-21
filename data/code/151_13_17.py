import itertools

def validate_lists(list1, list2):
    if not all(isinstance(item, (int, str)) for item in list1 + list2):
        raise ValueError("Both lists should contain only integers and strings")
    return True

def combine_lists(list1, list2):
    validate_lists(list1, list2)
    combined = list(itertools.chain(list1, list2))
    return combined

if __name__ == '__main__':
    sample_list1 = [1, 5, 2, 8, 5]
    sample_list2 = ['a', 'b', 'c']
    combined_result = combine_lists(sample_list1, sample_list2)
    print(combined_result)