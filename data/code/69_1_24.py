class IndexAccessor:

    def __init__(self, elements):
        self.elements = elements

    def get_element(self, index):
        if not 0 <= index < len(self.elements):
            return None
        return self.elements[index]
if __name__ == '__main__':
    sample_list = [100, 200, 300, 400, 500]
    accessor = IndexAccessor(sample_list)
    print(accessor.get_element(2))
    print(accessor.get_element(5))