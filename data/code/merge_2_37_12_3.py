import collections
class ItemCounter:
    def __init__(self):
        self._counts = collections.defaultdict(int)
    def add_item(self, item_id, quantity):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self._counts[item_id] += quantity
    def get_count(self, item_id):
        return self._counts.get(item_id, 0)
def process_data(items_list):
    counter = ItemCounter()
    for item in items_list:
        if isinstance(item, tuple) and len(item) == 2:
            try:
                count = int(item[1])
                counter.add_item(item[0], count)
            except ValueError as e:
                print(f"Error processing {item}: {e}")
    return dict(counter._counts)
if __name__ == '__main__':
    sample_data = [
        ("apple", 5),
        ("banana", 3),
        ("cherry", -2),
        ("date", 10),
        ("elderberry", 7)
    ]
    try:
        result = process_data(sample_data)
        print(result)
    except Exception as e:
        print(f"Unexpected error occurred: {e}")