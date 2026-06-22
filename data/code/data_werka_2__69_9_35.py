class IndexAccessor:

    def get_element(self, data_list, index):
        if not isinstance(data_list, list):
            raise TypeError('The first argument must be a list.')
        if not isinstance(index, int):
            raise TypeError('The index must be an integer.')
        try:
            return data_list[index]
        except IndexError:
            raise IndexError('Index out of bounds.')
if __name__ == '__main__':
    accessor = IndexAccessor()
    sample_list = [10, 20, 30, 40, 50]
    try:
        element = accessor.get_element(sample_list, 2)
        print(f'Element at index 2: {element}')
    except Exception as e:
        print(e)
    try:
        element = accessor.get_element(sample_list, 10)
        print(f'Element at index 10: {element}')
    except Exception as e:
        print(e)
    try:
        element = accessor.get_element(sample_list, -1)
        print(f'Element at index -1: {element}')
    except Exception as e:
        print(e)