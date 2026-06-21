class ListAccessor:
    def __init__(self, data):
        self.data = data

    def get_third(self):
        return self.data[2]

    def get_length(self):
        return len(self.data)

if __name__ == '__main__':
    sample = [100, 200, 300, 400, 500]
    accessor = ListAccessor(sample)
    print(accessor.get_third())
    print(accessor.get_length())