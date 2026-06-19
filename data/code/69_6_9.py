class ListDictInterface:

    def __init__(self, elements):
        self.elements = elements

    def __getitem__(self, key):
        if isinstance(key, int) or (isinstance(key, str) and key.isdigit()):
            index = int(key)
            if 0 <= index < len(self.elements):
                return self.elements[index]
            else:
                raise IndexError('Index out of range')
        else:
            raise TypeError('Key must be an integer or a string representing an integer')

    def __setitem__(self, key, value):
        if isinstance(key, int) or (isinstance(key, str) and key.isdigit()):
            index = int(key)
            if 0 <= index < len(self.elements):
                self.elements[index] = value
            else:
                raise IndexError('Index out of range')
        else:
            raise TypeError('Key must be an integer or a string representing an integer')

    def __len__(self):
        return len(self.elements)
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    list_dict_interface = ListDictInterface(sample_list)
    print(list_dict_interface['2'])
    list_dict_interface['3'] = 99
    print(list_dict_interface[3])