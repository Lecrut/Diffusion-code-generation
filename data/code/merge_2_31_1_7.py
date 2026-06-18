def filter_items(items_list):
    for item in items_list:
        if isinstance(item, dict) and 'status' in item and item['status'] == 'active':
            print(f"{item.get('name', 'Unknown')}")
if __name__ == '__main__':
    sample_data = [
        {'id': 101, 'name': 'Item Alpha', 'status': 'active'},
        {'id': 102, 'name': 'Item Beta', 'status': 'inactive'},
        {'id': 103, 'name': 'Item Gamma', 'status': 'active'},
        {'id': 104, 'name': 'Item Delta', 'status': 'pending'}
    ]
    filter_items(sample_data)