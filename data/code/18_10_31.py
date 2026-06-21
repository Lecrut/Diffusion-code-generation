def compare_first_two_elements(lst):
    first_element = lst[0]
    second_element = lst[1]
    return first_element > second_element

if __name__ == '__main__':
    sample_list_1 = [8, 3]
    result_1 = compare_first_two_elements(sample_list_1)
    print(f"Is the first element of {sample_list_1} greater than the second? {result_1}")

    sample_list_2 = [4.5, 4.5]
    result_2 = compare_first_two_elements(sample_list_2)
    print(f"Is the first element of {sample_list_2} greater than the second? {result_2}")