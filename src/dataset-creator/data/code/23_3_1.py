class StringItem:
    def __init__(self, value):
        self._value = str(value).strip().lower()
    @property
    def value(self):
        return self._value
    def normalize(self):
        cleaned = self.value.strip().replace(" ", "_")
        if not any(c.isalnum() or c == "_" for c in cleaned):
            raise ValueError(f"Invalid characters found: {self._value}")
        return StringItem(cleaned)
class StorageManager:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.items = []
    def add(self, item_value):
        if len(self.items) >= self.capacity:
            raise OverflowError("Storage full")
        try:
            new_item = StringItem(item_value).normalize()
        except ValueError as e:
            print(f"Normalization failed for '{item_value}': {e}")
            return False
        self.items.append(new_item.value)
        return True
    def get_all(self):
        return list(set(self.items))
if __name__ == '__main__':
    manager = StorageManager(capacity=50)
    samples = ["  Hello World! ", "HELLO_WORLD", "", "invalid@char#"]
    for sample in samples:
        result = manager.add(sample)
        if result:
            print(f"Added normalized value")
    final_list = manager.get_all()
    print("Final unique items:", sorted(final_list))