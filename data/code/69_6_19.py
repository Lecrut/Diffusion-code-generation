class ListDictInterface:

    def __init__(self, elements):
        self.elements = elements

    def __getitem__(self, key):
        if isinstance(key, int) and 0 <= key < len(self.elements):
            return self.elements[key]
        else:
            raise KeyError('Index out of range or not an integer')

    def __setitem__(self, key, value):
        if isinstance(key, int) and 0 <= key < len(self.elements):
            self.elements[key] = value
        else:
            raise KeyError('Index out of range or not an integer')

    def __len__(self):
        return len(self.elements)

    def __repr__(self):
        return repr(self.elements)
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    list_dict_interface = ListDictInterface(sample_list)
    print(list_dict_interface[2])
    list_dict_interface[2] = 300
    print(list_dict_interface)