import collections
class ItemCounter:
    def __init__(self):
        self._data = collections.defaultdict(int)
    def add_item(self, item_id, quantity):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self._data[item_id] += quantity
    def get_count(self, item_id):
        return self._data.get(item_id, 0)
def process_items(items_list):
    counter = ItemCounter()
    for item in items_list:
        if isinstance(item, tuple) and len(item) == 2:
            try:
                count = int(item[1])
                counter.add_item(item[0], count)
            except ValueError as e:
                print(f"Error processing {item}: {e}")
    return dict(counter._data)
if __name__ == '__main__':
    sample_data = [
        ('apple', 5),
        ('banana', 3),
        ('orange', -2),
        ('apple', 10),
        ('grape', 7),
    ]
    try:
        result = process_items(sample_data)
        print("Final counts:", result)
    except Exception as e:
        print(f"Unexpected error occurred: {e}")