def count_non_string_elements(lst):
    non_string_count = sum((1 for element in lst if not isinstance(element, str)))
    return non_string_count
if __name__ == '__main__':
    sample_list = ['a', 2, 'b', 3.5, True]
    print(count_non_string_elements(sample_list))