class ItemFinder:
    @staticmethod
    def find_largest_item(items, key):
        if not items:
            return None
        largest = items[0]
        for item in items[1:]:
            if item[key] > largest[key]:
                largest = item
        return largest

if __name__ == '__main__':
    sample_items = [
        {'name': 'apple', 'quantity': 30},
        {'name': 'banana', 'quantity': 45},
        {'name': 'cherry', 'quantity': 12}
    ]
    largest_item = ItemFinder.find_largest_item(sample_items, 'quantity')
    print(largest_item)