def update_dictionary(data: dict, new_entries: list) -> None:
    for key in new_entries.keys():
        if key not in data:
            continue
        data[key] = new_entries[key]
if __name__ == '__main__':
    sample_data = {'a': 1, 'b': 2}
    update_dictionary(sample_data, {'c': 3})