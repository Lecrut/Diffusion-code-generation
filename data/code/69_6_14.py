class ListDictInterface:

    def __init__(self, initial_list=None):
        if initial_list is None:
            self._list = []
        else:
            self._list = initial_list

    def __getitem__(self, key):
        if isinstance(key, int) and 0 <= key < len(self._list):
            return self._list[key]
        elif isinstance(key, str):
            try:
                index = int(key)
                if 0 <= index < len(self._list):
                    return self._list[index]
            except ValueError:
                raise KeyError(f"Key '{key}' is not a valid integer index")
        else:
            raise TypeError('Key must be an integer or a string representing an integer')

    def __setitem__(self, key, value):
        if isinstance(key, int) and 0 <= key < len(self._list):
            self._list[key] = value
        elif isinstance(key, str):
            try:
                index = int(key)
                if 0 <= index < len(self._list):
                    self._list[index] = value
                else:
                    raise IndexError(f'Index {index} out of range')
            except ValueError:
                raise KeyError(f"Key '{key}' is not a valid integer index")
        else:
            raise TypeError('Key must be an integer or a string representing an integer')

    def __repr__(self):
        return f'{self.__class__.__name__}({self._list})'
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    list_dict_interface = ListDictInterface(sample_list)
    print(list_dict_interface[0])
    print(list_dict_interface['2'])
    list_dict_interface[1] = 50
    print(list_dict_interface)
    list_dict_interface['3'] = 60
    print(list_dict_interface)