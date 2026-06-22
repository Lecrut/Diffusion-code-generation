class ListAccessor:

    def __init__(self, elements):
        self.elements = elements

    def get(self, index):
        if not isinstance(index, int):
            raise TypeError('Index must be an integer')
        if index < 0 or index >= len(self.elements):
            raise IndexError('Index out of range')
        return self.elements[index]
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    accessor = ListAccessor(sample_list)
    print(accessor.get(2))