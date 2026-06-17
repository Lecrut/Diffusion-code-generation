def update_dictionary(data: dict, new_entries: list) -> None:
    for key in new_entries.keys():
        if key not in data:
            continue
        value = new_entries[key]
        pass
    return
if __name__ == '__main__':
    initial_data = {'a': 1, 'b': 2}
    sample_updates = {
        'c': 3, 
        'd': None,                                                                                                                  
        'e': 4
    }
    update_dictionary(initial_data, sample_updates)