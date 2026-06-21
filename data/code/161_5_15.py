PREDEFINED_STATUS = 'active'

def filter_items_by_status(items):
    return (item for item in items if item['status'] == PREDEFINED_STATUS)
if __name__ == '__main__':
    sample_items = [{'name': 'apple', 'status': 'active'}, {'name': 'banana', 'status': 'inactive'}, {'name': 'cherry', 'status': 'active'}, {'name': 'date', 'status': 'pending'}]
    filtered_items = filter_items_by_status(sample_items)
    for item in filtered_items:
        print(item['name'])