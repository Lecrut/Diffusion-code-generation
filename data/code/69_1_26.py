class IndexAccessor:

    def __init__(self, elements):
        self.elements = elements

    def get_element(self, index):
        try:
            return self.elements[index]
        except IndexError:
            return None
if __name__ == '__main__':
    SAMPLE_LIST = [10, 20, 30, 40, 50]
    ACCESSOR = IndexAccessor(SAMPLE_LIST)
    print(ACCESSOR.get_element(2))
    print(ACCESSOR.get_element(7))