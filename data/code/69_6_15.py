class ListDict:

    def __init__(self, data):
        self.data = data

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __delitem__(self, key):
        del self.data[key]

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        return iter(self.data)
if __name__ == '__main__':
    sample_list = [10, 20, 30]
    list_dict = ListDict(sample_list)
    print(list_dict[0])
    list_dict[1] = 25
    print(list_dict)
    del list_dict[2]
    print(len(list_dict))