from collections import Counter

class InventoryCounter:
    @staticmethod
    def count_frequencies(item_names):
        return dict(Counter(item_names))

if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
    frequencies = InventoryCounter.count_frequencies(sample_items)
    print(frequencies)