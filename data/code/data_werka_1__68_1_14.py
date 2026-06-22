def find_element_differences(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Both lists must have the same length.")
    differences = [abs(a - b) for a, b in zip(list1, list2)]
    return differences

if __name__ == '__main__':
    sample_list_a = [7, 3, 9, 2]
    sample_list_b = [4, 8, 5, 6]
    try:
        result = find_element_differences(sample_list_a, sample_list_b)
        print(result)
    except ValueError as e:
        print(e)