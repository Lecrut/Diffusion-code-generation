class ItemFilter:
    def __init__(self, items):
        self.items = items

    def filter_by_status(self, status):
        return (item for item in self.items if item['status'] == status)

if __name__ == '__main__':
    sample_items = [
        {'name': 'apple', 'status': 'available'},
        {'name': 'banana', 'status': 'unavailable'},
        {'name': 'cherry', 'status': 'available'}
    ]
    filter_instance = ItemFilter(sample_items)
    available_items = filter_instance.filter_by_status('available')
    print(list(available_items))