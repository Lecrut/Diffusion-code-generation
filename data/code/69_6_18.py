class ListDictInterface:

    def __init__(self, elements):
        self.elements = elements

    def __getitem__(self, key):
        if isinstance(key, int):
            return self.elements[key]
        elif isinstance(key, str) and key.isdigit():
            return self.elements[int(key)]
        else:
            raise KeyError('Key must be an integer or a string representing an integer')

    def __setitem__(self, key, value):
        if isinstance(key, int):
            self.elements[key] = value
        elif isinstance(key, str) and key.isdigit():
            self.elements[int(key)] = value
        else:
            raise KeyError('Key must be an integer or a string representing an integer')

    def __len__(self):
        return len(self.elements)

    def __repr__(self):
        return repr(self.elements)
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    list_dict_interface = ListDictInterface(sample_list)
    print(list_dict_interface[0])
    print(list_dict_interface['2'])
    list_dict_interface[1] = 25
    print(list_dict_interface.elements)
    list_dict_interface['3'] = 45
    print(list_dict_interface.elements)
    print(len(list_dict_interface))