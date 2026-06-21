import bisect

class SortedItemList:
    def __init__(self):
        self.items = []

    def add_item(self, item_name):
        bisect.insort(self.items, item_name)

    def search_item(self, item_name):
        index = bisect.bisect_left(self.items, item_name)
        if index < len(self.items) and self.items[index] == item_name:
            return True
        return False

if __name__ == '__main__':
    item_list = SortedItemList()
    sample_items = ["Apple", "Banana", "Cherry"]
    
    for item in sample_items:
        item_list.add_item(item)
    
    search_items = ["Banana", "Grape", "Apple"]
    results = [item_list.search_item(item) for item in search_items]
    
    print(results)