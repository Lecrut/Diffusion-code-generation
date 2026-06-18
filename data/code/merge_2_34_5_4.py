def merge_dicts(main_data: list[dict], new_entries: list[dict]) -> list[dict]:
    seen_ids = set()
    merged_list = []
    for item in main_data + new_entries:
        if 'id' not in item or isinstance(item['id'], str):
            continue
        entry_id = item.get('id')
        if entry_id and entry_id not in seen_ids:
            seen_ids.add(entry_id)
            merged_list.append(dict(item))
    return merged_list
if __name__ == '__main__':
    main_dataset = [
        {'id': 1, 'name': 'Alice', 'role': 'Admin'},
        {'id': 2, 'name': 'Bob', 'role': 'Editor'}
    ]
    new_entries = [
        {'id': 3, 'name': 'Charlie', 'role': 'Viewer'},
        {'id': 1, 'name': 'Alice Duplicate', 'role': 'Admin'},
        {'id': 4, 'name': 'Diana', 'role': 'Editor'}
    ]
    final_dataset = merge_dicts(main_dataset, new_entries)
    print(final_dataset)