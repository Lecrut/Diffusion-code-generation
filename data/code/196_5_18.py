import itertools

def validate_lists(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise ValueError("Both inputs must be lists.")
    return list1, list2

def join_lists_with_itertools(list1, list2):
    it1 = iter(list1)
    it2 = iter(list2)
    return itertools.chain(it1, it2)

if __name__ == '__main__':
    list_a = [1, 2, 3]
    list_b = ['a', 'b', 'c']
    validated_lists = validate_lists(list_a, list_b)
    result_generator = join_lists_with_itertools(*validated_lists)
    final_list = list(result_generator)
    print(final_list)