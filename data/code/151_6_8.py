def validate_lists(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise ValueError("Both arguments must be lists")

def extend_list_in_place(list1, list2):
    validate_lists(list1, list2)
    list1.extend(list2)

if __name__ == '__main__':
    sample_list1 = [1, 2, 3]
    sample_list2 = [4, 5, 6]
    extend_list_in_place(sample_list1, sample_list2)
    print(sample_list1)