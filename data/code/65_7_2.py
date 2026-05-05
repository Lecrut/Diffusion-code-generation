class CustomList:
    def __init__(self, data):
        self._data = data
    def __getitem__(self, index):
        return self._data[index]
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    my_list = CustomList(sample_list)
    print(f"Accessing element at index 0: {my_list[0]}")
    print(f"Accessing element at index 2: {my_list[2]}")
    print(f"Accessing element at index 4: {my_list[4]}")
    try:
        print(f"Accessing element at index 5: {my_list[5]}")
    except IndexError as e:
        print(f"Caught expected error: {e}")