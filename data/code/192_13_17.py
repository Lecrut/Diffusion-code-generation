def validate_input(input_list):
    if not isinstance(input_list, list):
        raise ValueError("Input must be a list")
    return input_list

def find_common_items(list1, list2):
    set1 = validate_input(list1)
    set2 = validate_input(list2)
    return list(set1.intersection(set2))

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [4, 5, 6, 7, 8]
    common_items = find_common_items(sample_list1, sample_list2)
    print(f"Intersection of {sample_list1} and {sample_list2}: {common_items}")

    sample_list3 = ['apple', 'banana', 'cherry']
    sample_list4 = ['banana', 'date', 'apple']
    common_items = find_common_items(sample_list3, sample_list4)
    print(f"Intersection of {sample_list3} and {sample_list4}: {common_items}")

    sample_list5 = [10, 20, 30]
    sample_list6 = [30, 10, 40]
    common_items = find_common_items(sample_list5, sample_list6)
    print(f"Intersection of {sample_list5} and {sample_list6}: {common_items}")