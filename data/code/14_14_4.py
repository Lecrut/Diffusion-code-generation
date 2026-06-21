class ListAccessor:
    def __init__(self, values):
        self.data = values

    def get_item(self, index):
        return self.data[index]

    def get_third_element(self):
        return self.data[2]

if __name__ == '__main__':
    my_list = ['alpha', 'beta', 'gamma', 'delta', 'epsilon']
    accessor = ListAccessor(my_list)
    print(accessor.get_third_element())
    print(accessor.get_item(2))