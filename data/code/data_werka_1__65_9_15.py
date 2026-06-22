class ListAccessor:

    def __init__(self, data_list):
        self.data_list = data_list

    def get(self, index):
        if 0 <= index < len(self.data_list):
            return self.data_list[index]
        else:
            raise IndexError('Position out of bounds')
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    accessor = ListAccessor(sample_list)
    try:
        print(accessor.get(2))
        print(accessor.get(5))
    except IndexError as e:
        print(f'Error: {e}')