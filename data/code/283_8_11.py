def is_tuple(element):
    return isinstance(element, tuple)

def count_non_tuples(items):
    non_tuple_count = sum(1 for item in items if not is_tuple(item))
    return non_tuple_count

if __name__ == '__main__':
    sample_list = [("apple", "banana"), 42, "kiwi", (5,), 3.14]
    non_tuple_elements_count = count_non_tuples(sample_list)
    print(non_tuple_elements_count)