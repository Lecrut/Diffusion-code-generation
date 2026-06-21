class Item:
    def __init__(self, value):
        self.value = value

def sort_items(items):
    items.sort(key=lambda item: item.value)

if __name__ == '__main__':
    sample_items = [Item(5), Item(2), Item(8), Item(1), Item(9), Item(3)]
    print("Original list of values:", [item.value for item in sample_items])
    sort_items(sample_items)
    print("Sorted list of values:", [item.value for item in sample_items])