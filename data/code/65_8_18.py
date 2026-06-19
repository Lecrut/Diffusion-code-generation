class ListAccessor:

    def __init__(self, data):
        self.data = data

    def get_element_by_position(self, index):
        if not 0 <= index < len(self.data):
            raise IndexError('Index out of bounds')
        return self.data[index]
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    accessor = ListAccessor(sample_list)
    try:
        print(accessor.get_element_by_position(2))
        print(accessor.get_element_by_position(-1))
    except IndexError as e:
        print(e)
    try:
        print(accessor.get_element_by_position(5))
    except IndexError as e:
        print(e)