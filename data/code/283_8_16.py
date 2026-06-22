def count_non_tuple_elements(lst):
    return sum(1 for item in lst if not isinstance(item, tuple))

if __name__ == '__main__':
    sample_list = [(1, 2), 'string', [3, 4], (5,)]
    print(count_non_tuple_elements(sample_list))