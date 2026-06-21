class ListAccessor:
    def __init__(self, items):
        self.items = items

    def get_last(self):
        if self.items:
            return self.items[-1]
        return None

    def get_count(self):
        return len(self.items)

if __name__ == '__main__':
    sample_data = [100, 200, 300, 400, 500]
    accessor = ListAccessor(sample_data)
    print(accessor.get_last())
    print(accessor.get_count())