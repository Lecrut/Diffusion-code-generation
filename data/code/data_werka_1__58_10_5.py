class ListAccessor:
    def __init__(self, items):
        self.items = items

    def get_first_item(self):
        return self.items[0] if self.items else None

if __name__ == '__main__':
    sample_list = [15, 30, 45, 60]
    accessor = ListAccessor(sample_list)
    print(accessor.get_first_item())