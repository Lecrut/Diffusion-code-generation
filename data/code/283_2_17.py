def count_non_string_elements(lst):
    return sum(not isinstance(item, str) for item in lst)

if __name__ == '__main__':
    sample_list = ['hello', 42, 'world', None, True]
    print(count_non_string_elements(sample_list))