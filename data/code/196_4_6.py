def validate_input(input_list):
    if not isinstance(input_list, list):
        raise ValueError("Input must be a list")

def concatenate_lists(list1, list2):
    validate_input(list1)
    validate_input(list2)
    return list1 + list2

if __name__ == '__main__':
    sample_list1 = [1, 2, 3]
    sample_list2 = ['a', 'b', 'c']
    result = concatenate_lists(sample_list1, sample_list2)
    print(result)