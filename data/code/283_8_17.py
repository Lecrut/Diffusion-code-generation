def count_non_tuples(elements):
    non_tuple_count = 0
    for element in elements:
        if not isinstance(element, tuple):
            non_tuple_count += 1
    return non_tuple_count

if __name__ == '__main__':
    sample_list = [("apple", "banana"), "orange", 42, (1, 2), "kiwi"]
    result = count_non_tuples(sample_list)
    print(result)