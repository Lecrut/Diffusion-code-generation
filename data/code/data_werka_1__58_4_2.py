class ListHandler:
    def __init__(self, items):
        self.items = items

    @classmethod
    def from_dict(cls, item_dict):
        return cls(list(item_dict.values()))

    def get_first_item(self):
        return self.items[0] if self.items else None

if __name__ == '__main__':
    sample_data = {'a': 1, 'b': 2, 'c': 3}
    handler = ListHandler.from_dict(sample_data)
    first_item = handler.get_first_item()
    print(first_item)