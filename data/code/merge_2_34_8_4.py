def update_dictionary(data: dict, new_items: list) -> None:
    for item in new_items:
        if isinstance(item, tuple):
            data[item[0]] = item[1]
if __name__ == '__main__':
    my_dict = {'a': 1}
    update_dictionary(my_dict, [('b', 2), ('c', None)])