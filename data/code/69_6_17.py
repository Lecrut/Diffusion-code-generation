class ListDictInterface:

    def __init__(self, elements):
        self.elements = elements

    def __getitem__(self, key):
        try:
            index = int(key)
            if 0 <= index < len(self.elements):
                return self.elements[index]
            raise IndexError(f'Index {index} out of range')
        except ValueError:
            raise KeyError(f'Key {key} not found')

    def __setitem__(self, key, value):
        try:
            index = int(key)
            if 0 <= index < len(self.elements):
                self.elements[index] = value
            else:
                raise IndexError(f'Index {index} out of range')
        except ValueError:
            raise KeyError(f'Key {key} not found')
if __name__ == '__main__':
    mixed_list = [10, 'hello', 3.14, True, [1, 2], None]
    list_dict = ListDictInterface(mixed_list)
    print(list_dict['0'])
    print(list_dict[2])
    list_dict['3'] = False
    print(list_dict)