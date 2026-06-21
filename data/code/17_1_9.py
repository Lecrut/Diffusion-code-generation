class ListAccessor:
    def __init__(self, data):
        self.data = data

    def get_last_item(self):
        if not self.data:
            return None
        return self.data[len(self.data) - 1]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    accessor = ListAccessor(sample_list)
    result = accessor.get_last_item()
    print(result)