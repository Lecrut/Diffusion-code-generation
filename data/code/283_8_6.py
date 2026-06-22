def count_non_tuples(lst):
    return sum(not isinstance(item, tuple) for item in lst)

if __name__ == '__main__':
    sample_list = [(1, 2), 'string', (3, 4), 5, [6, 7], {'a': 8}]
    print(count_non_tuples(sample_list))