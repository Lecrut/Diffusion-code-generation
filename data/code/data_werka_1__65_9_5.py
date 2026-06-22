class ListAccessor:

    def __init__(self, data_list):
        self.data_list = data_list

    def get(self, index):
        if 0 <= index < len(self.data_list):
            return self.data_list[index]
        else:
            raise IndexError('Index out of bounds')
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    accessor = ListAccessor(sample_data)
    try:
        print(accessor.get(2))
        print(accessor.get(0))
        print(accessor.get(4))
        print(accessor.get(5))
    except IndexError as e:
        print(f'Error: {e}')