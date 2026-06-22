def count_non_strings(lst):
    non_string_count = sum((1 for item in lst if not isinstance(item, str)))
    return non_string_count
if __name__ == '__main__':
    sample_list = [1, 'hello', 3.14, 'world', None]
    print(count_non_strings(sample_list))