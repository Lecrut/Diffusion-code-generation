class ListAccessor:
    def __init__(self, data):
        self.data = data

    def get_sublist(self, start, end):
        return self.data[start:end]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    accessor = ListAccessor(sample_list)
    sublist = accessor.get_sublist(2, 5)
    print(sublist)