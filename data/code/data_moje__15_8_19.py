class ListAccessor:
    def __init__(self, data):
        self.data = data

    def get_pre_last(self):
        return self.data[-2]

    def get_length(self):
        return len(self.data)

if __name__ == '__main__':
    sample_values = [100, 200, 300, 400]
    accessor = ListAccessor(sample_values)
    print(accessor.get_pre_last())
    print(accessor.get_length())