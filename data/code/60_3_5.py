class ListAccessor:
    def __init__(self, data):
        self.data = data

    def get_last_element(self):
        return self.data[-1]

if __name__ == '__main__':
    sample_list = [100, 200, 300, 400, 500]
    accessor = ListAccessor(sample_list)
    print(accessor.get_last_element())