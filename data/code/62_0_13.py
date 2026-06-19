class ListAccessor:
    def __init__(self, items):
        self.items = items

    def get_second_item(self):
        return self.items[1]

if __name__ == '__main__':
    sample_list = ['a', 'b', 'c', 'd']
    accessor = ListAccessor(sample_list)
    second_item = accessor.get_second_item()
    print(second_item)