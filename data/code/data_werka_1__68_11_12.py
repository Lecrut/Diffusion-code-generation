def validate_lists(list1, list2):
    if not (isinstance(list1, list) and isinstance(list2, list)):
        raise ValueError("Both inputs must be lists.")
    if len(list1) != len(list2):
        raise ValueError("Both lists must have the same length.")

def absolute_difference_generator(list1, list2):
    validate_lists(list1, list2)
    for num1, num2 in zip(list1, list2):
        yield abs(num1 - num2)

if __name__ == '__main__':
    try:
        sample_list1 = [8, 16, 24, 32]
        sample_list2 = [4, 8, 12, 16]
        for diff in absolute_difference_generator(sample_list1, sample_list2):
            print(diff)
    except ValueError as e:
        print(e)