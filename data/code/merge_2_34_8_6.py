def update_dictionary(data: dict, new_entries: dict) -> None:
    for key, value in new_entries.items():
        data[key] = value
if __name__ == '__main__':
    my_dict = {'a': 1, 'b': 2}
    updates = {'c': 3, 'd': 4}
    update_dictionary(my_dict, updates)
    print(f"Updated dictionary: {my_dict}")