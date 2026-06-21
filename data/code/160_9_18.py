import bisect

def validate_item_name(item_name):
    if not item_name:
        raise ValueError('Item name cannot be empty')

class SortedItemList:

    def __init__(self):
        self.items = []

    def add_item(self, item_name):
        validate_item_name(item_name)
        bisect.insort(self.items, item_name)

    def get_index(self, item_name):
        validate_item_name(item_name)
        index = bisect.bisect_left(self.items, item_name)
        if index < len(self.items) and self.items[index] == item_name:
            return index
        else:
            raise ValueError('Item not found')
if __name__ == '__main__':
    sample_data = ['Apple', 'Banana', 'Cherry']
    sorted_item_list = SortedItemList()
    for item in sample_data:
        sorted_item_list.add_item(item)
    print(sorted_item_list.items)
    print(f"Index of 'Banana': {sorted_item_list.get_index('Banana')}")