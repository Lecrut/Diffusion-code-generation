class ListAccessor:

    def __init__(self, elements):
        self.elements = elements

    def get_element(self, position):
        if not 0 <= position < len(self.elements):
            raise ValueError('Position out of range')
        return self.elements[position]
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    accessor = ListAccessor(sample_list)
    print(accessor.get_element(2))