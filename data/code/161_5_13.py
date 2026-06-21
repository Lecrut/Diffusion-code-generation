class ItemFilter:
    def __init__(self, items):
        self.items = items

    def filter_by_status(self, status):
        return (item for item in self.items if item['status'] == status)

if __name__ == '__main__':
    sample_items = [
        {'name': 'apple', 'status': 'active'},
        {'name': 'banana', 'status': 'inactive'},
        {'name': 'cherry', 'status': 'active'},
        {'name': 'date', 'status': 'pending'}
    ]
    filter_obj = ItemFilter(sample_items)
    active_items = list(filter_obj.filter_by_status('active'))
    print(active_items)