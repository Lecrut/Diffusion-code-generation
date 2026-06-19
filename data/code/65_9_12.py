class ListAccessor:

    def __init__(self, data_list):
        self.data_list = data_list

    def get(self, index):
        if 0 <= index < len(self.data_list):
            return self.data_list[index]
        else:
            raise IndexError('Position out of bounds')
if __name__ == '__main__':
    sample_data = [15, 25, 35, 45, 55]
    accessor = ListAccessor(sample_data)
    try:
        print(accessor.get(2))
    except IndexError as e:
        print(f'Error: {e}')