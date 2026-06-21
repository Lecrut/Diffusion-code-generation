import itertools

def validate_lists(list1, list2):
    if not all(isinstance(item, (int, str)) for item in list1 + list2):
        raise ValueError("Both lists must contain only integers or strings")
    return list1, list2

def combine_lists(list1, list2):
    validated_list1, validated_list2 = validate_lists(list1, list2)
    combined = itertools.chain(validated_list1, validated_list2)
    return list(combined)

if __name__ == '__main__':
    sample_list1 = [1, 5, 2, 8, 5]
    sample_list2 = ['a', 'b', 'c']
    result = combine_lists(sample_list1, sample_list2)
    print(result)