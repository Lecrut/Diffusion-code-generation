def filter_items(items, status):
    return (item for item in items if item['status'] == status)

if __name__ == '__main__':
    items = [
        {'name': 'Item 1', 'status': 'active'},
        {'name': 'Item 2', 'status': 'inactive'},
        {'name': 'Item 3', 'status': 'active'}
    ]
    filtered_items = filter_items(items, 'active')
    for item in filtered_items:
        print(item)