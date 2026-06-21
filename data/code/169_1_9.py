from collections import Counter

class InventoryCounter:
    def __init__(self):
        self.inventory_counts = {}

    @staticmethod
    def count_items(items):
        return dict(Counter(items))

    @staticmethod
    def sort_by_count(frequency_dict):
        return sorted(frequency_dict.items(), key=lambda x: x[1], reverse=True)

    def process_inventory(self, items):
        frequency_dict = self.count_items(items)
        sorted_counts = self.sort_by_count(frequency_dict)
        return dict(sorted_counts)

if __name__ == '__main__':
    inventory_manager = InventoryCounter()
    sample_items = ["apple", "banana", "apple", "orange", "banana", "banana"]
    result = inventory_manager.process_inventory(sample_items)
    print(result)