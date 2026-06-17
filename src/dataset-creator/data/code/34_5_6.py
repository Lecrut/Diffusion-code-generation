def merge_dicts(main_data: list[dict], new_entries: list[dict]) -> list[dict]:
    for entry in new_entries:
        is_duplicate = False
        for existing_entry in main_data:
            if dict(entry) == dict(existing_entry):
                is_duplicate = True
                break
        if not is_duplicate:
            main_data.append(entry)
    return main_data
if __name__ == '__main__':
    dataset = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
    new_items = [
        {'id': 3, 'name': 'Charlie'}, 
        {'id': 4, 'name': 'David'}, 
        {'id': 1, 'name': 'Alice'}
    ]
    result = merge_dicts(dataset.copy(), new_items)
    print(result)