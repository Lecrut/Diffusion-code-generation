class ListAccessor:
    def __init__(self, data):
        self.data = data

    def get_boundary(self):
        if not self.data:
            raise ValueError("List must not be empty")
        return (self.data[0], self.data[-1])

if __name__ == '__main__':
    items = [42, 17, 99, 3, 88]
    accessor = ListAccessor(items)
    print(accessor.get_boundary())