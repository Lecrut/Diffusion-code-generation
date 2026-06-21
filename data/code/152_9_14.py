def find_shared_elements(list1, list2):

    def validate_lists(l1, l2):
        if not all((isinstance(item, (int, float)) for item in l1 + l2)):
            raise ValueError('Both inputs must be lists of numbers.')
    validate_lists(list1, list2)
    set1 = set(list1)
    set2 = set(list2)
    shared_elements = set1.intersection(set2)
    return shared_elements
if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [4, 5, 6, 7, 8]
    result = find_shared_elements(sample_list1, sample_list2)
    print(result)