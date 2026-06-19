class ListManager:
    def __init__(self, items):
        self.items = items

    @classmethod
    def from_tuple(cls, item_tuple):
        return cls(list(item_tuple))

    def get_first_item(self):
        if self.items:
            return self.items[0]
        else:
            return None

if __name__ == '__main__':
    sample_tuple = (100, 200, 300, 400)
    manager_from_tuple = ListManager.from_tuple(sample_tuple)
    print(manager_from_tuple.get_first_item())

    sample_list = ['dog', 'cat', 'bird']
    manager_from_list = ListManager(sample_list)
    print(manager_from_list.get_first_item())