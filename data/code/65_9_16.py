class ListAccessor:

    def __init__(self, elements):
        self.elements = elements

    def get(self, index):
        try:
            return self.elements[index]
        except IndexError:
            raise IndexError('Index out of range')
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    accessor = ListAccessor(sample_list)
    print(accessor.get(2))
    print(accessor.get(4))
    try:
        print(accessor.get(10))
    except IndexError as e:
        print(e)