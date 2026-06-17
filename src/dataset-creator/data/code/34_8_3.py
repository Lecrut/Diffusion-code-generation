def update_dictionary(data: dict, new_items: list[tuple]) -> None:
    for key, value in new_items:
        if isinstance(key, str) and len(key.strip()) > 0:
            data[key] = value
if __name__ == '__main__':
    my_dict = {'a': 1}
    update_dictionary(my_dict, [('b', 2), ('c', 3)])
    print(dict(sorted(my_dict.items())))