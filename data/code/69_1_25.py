class IndexAccessor:
    DEFAULT_VALUE = None

    def __init__(self, elements):
        self.elements = elements

    def get_element(self, index):
        try:
            return self.elements[index]
        except IndexError:
            return IndexAccessor.DEFAULT_VALUE
if __name__ == '__main__':
    sample_list = [100, 200, 300, 400, 500]
    accessor = IndexAccessor(sample_list)
    print(accessor.get_element(1))
    print(accessor.get_element(5))