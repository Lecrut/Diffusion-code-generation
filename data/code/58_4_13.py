class ListManager:
    def __init__(self, items):
        self.items = items

    @classmethod
    def from_tuple(cls, item_tuple):
        return cls(list(item_tuple))

    def get_first_item(self):
        return self.items[0] if self.items else None

if __name__ == '__main__':
    sample_list_manager = ListManager([100, 200, 300])
    print(sample_list_manager.get_first_item())

    tuple_data = (400, 500, 600)
    tuple_list_manager = ListManager.from_tuple(tuple_data)
    print(tuple_list_manager.get_first_item())