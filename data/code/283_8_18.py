def count_non_tuples(items):
    non_tuple_count = 0
    for item in items:
        if not isinstance(item, tuple):
            non_tuple_count += 1
    return non_tuple_count

if __name__ == '__main__':
    sample_list = [1, "banana", (3, 4), {"key": "value"}, [5, 6]]
    count = count_non_tuples(sample_list)
    print(count)