class ListAccessor:
    def __init__(self, data):
        self.data = data

    def get_second_item(self):
        return self.data[1]

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry', 'date']
    accessor = ListAccessor(sample_list)
    second_item = accessor.get_second_item()
    print(second_item)