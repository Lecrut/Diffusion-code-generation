class ItemFinder:
    @staticmethod
    def find_largest_item(items, key):
        if not items:
            return None
        largest = max(items, key=lambda item: item[key])
        return largest

if __name__ == '__main__':
    sample_items = [
        {'name': 'apple', 'price': 1.2},
        {'name': 'banana', 'price': 0.8},
        {'name': 'cherry', 'price': 3.5}
    ]
    largest_item = ItemFinder.find_largest_item(sample_items, 'price')
    print(largest_item)