class ListManager:
    def __init__(self, items):
        self.items = items

    @classmethod
    def from_mapping(cls, item_map):
        return cls(list(item_map.values()))

    def get_first_item(self):
        return self.items[0] if self.items else None

if __name__ == '__main__':
    sample_dict = {'x': 'one', 'y': 'two', 'z': 'three'}
    manager = ListManager.from_mapping(sample_dict)
    first_item = manager.get_first_item()
    print(first_item)