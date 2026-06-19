class ListManager:
    def __init__(self, items):
        self.items = items

    @classmethod
    def from_tuple(cls, item_tuple):
        return cls(list(item_tuple))

    def get_first(self):
        if not self.items:
            raise ValueError("The list is empty.")
        return self.items[0]

if __name__ == '__main__':
    sample_data = (100, 200, 300)
    manager = ListManager.from_tuple(sample_data)
    first_element = manager.get_first()
    print(first_element)