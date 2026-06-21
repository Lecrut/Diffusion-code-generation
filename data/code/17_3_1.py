def _resolve_index(collection):
    return len(collection) - 1

def get_last_element(collection):
    if len(collection) == 0:
        raise IndexError("collection is empty")
    index = _resolve_index(collection)
    return collection[index]

if __name__ == '__main__':
    data_list = [99, 88, 77, 66, 55]
    data_tuple = (1, 2, 3)
    data_string = "python"
    data_set = {100, 200, 300}
    print(get_last_element(data_list))
    print(get_last_element(data_tuple))
    print(get_last_element(data_string))
    print(get_last_element(data_set))
    single_item = [42]
    print(get_last_element(single_item))