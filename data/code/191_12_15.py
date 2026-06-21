import itertools

def validate_lists(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise ValueError("Both inputs must be lists.")
    return list1, list2

def combine_lists(list1, list2):
    return list(itertools.chain(list1, list2))

if __name__ == '__main__':
    sample_list1 = [1, 2, 3]
    sample_list2 = ['a', 'b', 'c']
    
    validated_lists = validate_lists(sample_list1, sample_list2)
    combined_list = combine_lists(*validated_lists)
    
    print(combined_list)