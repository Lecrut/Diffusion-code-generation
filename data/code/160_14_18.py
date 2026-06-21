class ItemFilter:
    def __init__(self, items):
        self.items = items

    def filter_by_initial(self, initial):
        return [item for item in self.items if item.startswith(initial)]

if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'apricot', 'cherry', 'blueberry']
    filterer = ItemFilter(sample_items)
    filtered_apples = filterer.filter_by_initial('a')
    filtered_bananas = filterer.filter_by_initial('b')
    print(filtered_apples)
    print(filtered_bananas)