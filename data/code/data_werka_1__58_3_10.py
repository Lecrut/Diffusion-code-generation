class ListAccessor:
    def __init__(self, data):
        self.data = data

    def get_first_element(self):
        return self.data[0]

if __name__ == '__main__':
    data = [5, 10, 15]
    accessor = ListAccessor(data)
    print(accessor.get_first_element())