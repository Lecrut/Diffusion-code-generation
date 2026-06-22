def count_non_tuples(elements):
    non_tuple_count = sum(not isinstance(item, tuple) for item in elements)
    return non_tuple_count

if __name__ == '__main__':
    sample_list = [1, "apple", (3, 4), {"key": "value"}, [5, 6], None]
    non_tuple_count = count_non_tuples(sample_list)
    print(non_tuple_count)