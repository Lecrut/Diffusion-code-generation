import time
class ItemCounter:
    def __init__(self):
        self._counts = {}
    def add_item(self, item):
        if isinstance(item, int) and 0 <= item < len(self._counts):
            self._counts[item] += 1
    def get_count_at_index(self, index):
        return self._counts.get(index, 0)
if __name__ == '__main__':
    counter = ItemCounter()
    sample_items = [5, 3, 8, 2, 9, 7]
    for item in sample_items:
        counter.add_item(item)
    print(counter.get_count_at_index(0))