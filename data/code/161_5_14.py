def filter_items(items, status):
    return (item for item in items if item['status'] == status)

if __name__ == '__main__':
    items = [
        {'id': 1, 'name': 'Item 1', 'status': 'active'},
        {'id': 2, 'name': 'Item 2', 'status': 'inactive'},
        {'id': 3, 'name': 'Item 3', 'status': 'active'}
    ]
    status = 'active'
    filtered_items = filter_items(items, status)
    for item in filtered_items:
        print(item)