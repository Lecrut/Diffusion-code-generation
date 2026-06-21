def filter_items_by_status(items, status):
    return (item for item in items if item['status'] == status)

if __name__ == '__main__':
    sample_items = [
        {'id': 1, 'name': 'apple', 'status': 'active'},
        {'id': 2, 'name': 'banana', 'status': 'inactive'},
        {'id': 3, 'name': 'cherry', 'status': 'active'}
    ]
    target_status = 'active'
    filtered_items = filter_items_by_status(sample_items, target_status)
    for item in filtered_items:
        print(item)