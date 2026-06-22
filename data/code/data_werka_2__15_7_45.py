def are_lists_identical(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise ValueError("Both inputs must be lists.")
    
    try:
        return all(elem1 == elem2 for elem1, elem2 in zip(list1, list2))
    except TypeError:
        raise ValueError("All elements of the lists must be comparable.")

if __name__ == '__main__':
    sample_list1 = [100, 200, 300, 400, 500]
    sample_list2 = [100, 200, 300, 400, 500]
    sample_list3 = [100, 200, 300, 400, 600]
    
    try:
        print(are_lists_identical(sample_list1, sample_list2))
        print(are_lists_identical(sample_list1, sample_list3))
    except ValueError as e:
        print(e)