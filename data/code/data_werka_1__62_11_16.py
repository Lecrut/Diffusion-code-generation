class ListAccessor:
    def __init__(self, data):
        self.data = data

    def get_second(self):
        if len(self.data) > 1:
            return self.data[1]
        else:
            return None

if __name__ == '__main__':
    list_samples = {
        'list1': [10, 20, 30],
        'list2': [5],
        'list3': [],
        'list4': [1]
    }

    for name, data in list_samples.items():
        accessor = ListAccessor(data)
        print(f"{name}: {accessor.get_second()}")