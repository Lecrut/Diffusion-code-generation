def update_dictionary(data: dict, new_entries: list) -> None:
    for item in new_entries:
        if isinstance(item, tuple):
            data[item[0]] = item[1]
        elif len(item) == 2 and all(isinstance(k, str) and isinstance(v, (int, float)) for k, v in item):
            data[item[0]] = item[1]
if __name__ == '__main__':
    sample_data = {'a': 1, 'b': 2}
    new_updates = [('c', 3), ('d', 4.5)]
    update_dictionary(sample_data, new_updates)