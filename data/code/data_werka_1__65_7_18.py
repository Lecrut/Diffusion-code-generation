class CustomList:
    def __init__(self, data):
        self._data = data

    def validate_index(self, index):
        if not isinstance(index, int):
            raise TypeError("Index must be an integer")
        if index < 0 or index >= len(self._data):
            raise IndexError("Index out of range")

    def __getitem__(self, index):
        self.validate_index(index)
        return self._data[index]

if __name__ == '__main__':
    sample_values = [15, 25, 35, 45, 55]
    my_list = CustomList(sample_values)
    
    print(my_list[0])
    print(my_list[2])
    print(my_list[4])
    
    try:
        print(my_list[5])
    except IndexError as e:
        print(f"Caught expected error: {e}")