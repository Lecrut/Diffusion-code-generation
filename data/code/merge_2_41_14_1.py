import timeit
def count_list_elements():
    data = [10, 20, 30]
    return len(data)
def count_tuple_elements():
    data = (10, 20, 30)
    return len(data)
def count_set_elements():
    data = {10, 20, 30}
    return len(data)
def count_dict_elements():
    data = {'a': 1, 'b': 2, 'c': 3}
    return len(data)
if __name__ == '__main__':
    list_count = count_list_elements()
    tuple_count = count_tuple_elements()
    set_count = count_set_elements()
    dict_count = count_dict_elements()
    print(f"List elements: {list_count}")
    print(f"Tuple elements: {tuple_count}")
    print(f"Set elements: {set_count}")
    print(f"Dict elements: {dict_count}")
    list_time = timeit.timeit(count_list_elements, number=10000)
    tuple_time = timeit.timeit(count_tuple_elements, number=10000)
    set_time = timeit.timeit(count_set_elements, number=10000)
    dict_time = timeit.timeit(count_dict_elements, number=10000)
    print(f"List avg time: {list_time:.6f}s")
    print(f"Tuple avg time: {tuple_time:.6f}s")
    print(f"Set avg time: {set_time:.6f}s")
    print(f"Dict avg time: {dict_time:.6f}s")