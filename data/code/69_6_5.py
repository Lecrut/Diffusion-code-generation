class ListDictInterface:

    def __init__(self, elements):
        self.elements = elements

    def __getitem__(self, key):
        if isinstance(key, int) and 0 <= key < len(self.elements):
            return self.elements[key]
        elif isinstance(key, str):
            try:
                index = int(key)
                if 0 <= index < len(self.elements):
                    return self.elements[index]
            except ValueError:
                raise KeyError(f'Key {key} not found')
        raise KeyError(f'Key {key} not found')

    def __setitem__(self, key, value):
        if isinstance(key, int) and 0 <= key < len(self.elements):
            self.elements[key] = value
        elif isinstance(key, str):
            try:
                index = int(key)
                if 0 <= index < len(self.elements):
                    self.elements[index] = value
                else:
                    raise IndexError(f'Index {index} out of range')
            except ValueError:
                raise KeyError(f'Key {key} not found')
if __name__ == '__main__':
    sample_list = [10, 'hello', 3.14, True, [1, 2], None]
    list_dict_interface = ListDictInterface(sample_list)
    print(list_dict_interface[0])
    print(list_dict_interface['2'])
    list_dict_interface['3'] = 'world'
    print(list_dict_interface['3'])
    try:
        print(list_dict_interface[10])
    except Exception as e:
        print(e)
    try:
        print(list_dict_interface['abc'])
    except Exception as e:
        print(e)