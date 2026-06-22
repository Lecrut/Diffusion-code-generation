class ListAccessor:

    def __init__(self, data_list):
        self.data_list = data_list

    def get(self, index):
        if 0 <= index < len(self.data_list):
            return self.data_list[index]
        else:
            raise IndexError('Position out of bounds')
if __name__ == '__main__':
    sample_list = [5, 15, 25, 35, 45]
    accessor = ListAccessor(sample_list)
    try:
        result = accessor.get(2)
        print(result)
    except IndexError as e:
        print(f'Error: {e}')
    try:
        out_of_bounds_result = accessor.get(10)
        print(out_of_bounds_result)
    except IndexError as e:
        print(f'Error: {e}')