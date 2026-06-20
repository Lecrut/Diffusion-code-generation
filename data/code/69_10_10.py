class IndexAccessor:

    def get_element(self, data_list, index):
        if 0 <= index < len(data_list):
            return data_list[index]
        else:
            raise IndexError('Index out of bounds')
if __name__ == '__main__':
    accessor = IndexAccessor()
    sample_list = [1, 2, 3, 4, 5]
    print(accessor.get_element(sample_list, 2))
    try:
        print(accessor.get_element(sample_list, 5))
    except IndexError as e:
        print(e)