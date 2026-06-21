class ItemFilter:
    def __init__(self, items):
        self.items = items

    def filter_by_initial(self, initial):
        return [item for item in self.items if item.startswith(initial)]

if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'apricot', 'cherry', 'blueberry']
    filter_obj = ItemFilter(sample_items)
    filtered_apple_items = filter_obj.filter_by_initial('a')
    print(filtered_apple_items)