import itertools

def validate_lists(list1, list2):
    if not all(isinstance(item, (list, tuple)) for item in [list1, list2]):
        raise ValueError("Both inputs must be lists or tuples")
    return list1, list2

def combine_and_chain(list1, list2):
    valid_list1, valid_list2 = validate_lists(list1, list2)
    return list(itertools.chain(valid_list1, valid_list2))

if __name__ == '__main__':
    sample_list1 = [1, 2, 3]
    sample_list2 = ['a', 'b', 'c']
    combined_list = combine_and_chain(sample_list1, sample_list2)
    print(combined_list)