from collections import Counter

class InventoryAggregator:
    @staticmethod
    def aggregate_inventory(item_counts):
        return dict(Counter(item_counts))

if __name__ == '__main__':
    sample_data = [
        ("apple", 10),
        ("banana", 5),
        ("apple", 15),
        ("orange", 8),
        ("banana", 12),
        ("apple", 7)
    ]
    total_inventory = InventoryAggregator.aggregate_inventory(sample_data)
    print(total_inventory)