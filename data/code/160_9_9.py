import bisect

class SortedItemList:

    def __init__(self):
        self.items = []

    def insert(self, item_name):
        bisect.insort(self.items, item_name)

    def search(self, item_name):
        index = bisect.bisect_left(self.items, item_name)
        if index != len(self.items) and self.items[index] == item_name:
            return True
        return False
if __name__ == '__main__':
    sample_data = ['Apple', 'Banana', 'Cherry']
    sorted_item_list = SortedItemList()
    for item in sample_data:
        sorted_item_list.insert(item)
    print(sorted_item_list.search('Banana'))
    print(sorted_item_list.search('Grape'))