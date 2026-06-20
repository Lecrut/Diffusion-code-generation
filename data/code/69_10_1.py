class IndexAccessor:

    def get_element(self, data_list, index):
        if 0 <= index < len(data_list):
            return data_list[index]
        else:
            raise IndexError('Index out of bounds')
if __name__ == '__main__':
    accessor = IndexAccessor()
    sample_list = [10, 20, 30, 40, 50]
    try:
        print(accessor.get_element(sample_list, 2))
        print(accessor.get_element(sample_list, 5))
    except IndexError as e:
        print(e)