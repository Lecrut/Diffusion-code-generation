def compare_first_two_elements(lst):
    first_element = lst[0]
    second_element = lst[1]
    return first_element > second_element

if __name__ == '__main__':
    sample_list = [8, 6]
    result = compare_first_two_elements(sample_list)
    print(f"Is the first element of {sample_list} greater than the second? {result}")