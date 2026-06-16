import re
class StringItem:
    def __init__(self, text):
        self._original = text
        if not isinstance(text, str):
            raise TypeError("Input must be a string")
        normalized_text = " ".join(re.sub(r'\s+', ' ', text.strip()).lower())
        super().__setattr__('_normalized', normalized_text)
    @property
    def original(self):
        return self._original
    @property
    def value(self):
        return self._normalized
class StringStorage:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.items = []
    def add_item(self, item_text):
        if len(self.items) >= self.capacity:
            raise OverflowError("Storage is full")
        new_item = StringItem(item_text)
        self.items.append(new_item)
    def get_all_values(self):
        return [item.value for item in self.items]
if __name__ == '__main__':
    storage = StringStorage(capacity=5)
    sample_items = ["Hello World", "  Python   Is Great!", "data, is: good.", "!@#$%^&*()"]
    for text in sample_items:
        try:
            storage.add_item(text)
        except OverflowError as e:
            print(f"Error adding item: {e}")
    all_values = storage.get_all_values()
    if len(all_values) > 0:
        result_string = " | ".join([f'Original:{v}, Normalized:{s}' for v, s in zip(storage.items[0].original, [storage.items[0].value])])
        print("Initialization Complete.")