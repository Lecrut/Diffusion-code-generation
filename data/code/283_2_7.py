def count_non_string_elements(lst):
    non_string_count = sum(not isinstance(item, str) for item in lst)
    return non_string_count

if __name__ == '__main__':
    sample_list = [1, "hello", 3.14, "world", True]
    print(count_non_string_elements(sample_list))