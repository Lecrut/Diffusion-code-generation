class CustomList:
    def __init__(self, data):
        self._data = data
    def __getitem__(self, index):
        return self._data[index]
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    my_list = CustomList(sample_data)
    print(my_list[0])
    print(my_list[2])
    print(my_list[4])
    print(my_list[1])