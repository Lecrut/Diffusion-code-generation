class ListAccessor:

    def __init__(self, elements):
        self.elements = elements

    def get_element(self, index):
        if not 0 <= index < len(self.elements):
            raise IndexError('Index out of bounds')
        return self.elements[index]
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    accessor = ListAccessor(sample_list)
    try:
        print(accessor.get_element(2))
        print(accessor.get_element(5))
    except IndexError as e:
        print(e)