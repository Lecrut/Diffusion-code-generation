import itertools

def validate_lists(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise ValueError("Both inputs must be lists.")
    return list1, list2

def combine_lists(list1, list2):
    validated_list1, validated_list2 = validate_lists(list1, list2)
    combined = itertools.chain(validated_list1, validated_list2)
    return list(combined)

if __name__ == '__main__':
    sample_list1 = [1, 5, 2, 8, 5]
    sample_list2 = [8, 3, 1, 9, 2]
    combined_result = combine_lists(sample_list1, sample_list2)
    print(combined_result)