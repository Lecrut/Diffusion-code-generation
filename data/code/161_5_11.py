def filter_items(items, status):
    return (item for item in items if item['status'] == status)

if __name__ == '__main__':
    sample_items = [
        {'name': 'Item 1', 'status': 'active'},
        {'name': 'Item 2', 'status': 'inactive'},
        {'name': 'Item 3', 'status': 'active'}
    ]
    active_items = filter_items(sample_items, 'active')
    for item in active_items:
        print(item)