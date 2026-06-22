class ItemCounter:
    def __init__(self, items):
        self.items = items

    def count_items(self):
        return len(self.items)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    counter = ItemCounter(sample_list)
    print(f"The number of items in the list is: {counter.count_items()}")