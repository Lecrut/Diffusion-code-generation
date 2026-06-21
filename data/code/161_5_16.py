def filter_items_by_status(items, status):
    return (item for item in items if item['status'] == status)

if __name__ == '__main__':
    sample_items = [
        {'name': 'apple', 'status': 'active'},
        {'name': 'banana', 'status': 'inactive'},
        {'name': 'cherry', 'status': 'active'},
        {'name': 'date', 'status': 'pending'}
    ]
    status_to_filter = 'active'
    filtered_items = filter_items_by_status(sample_items, status_to_filter)
    print(list(filtered_items))