class IndexAccessor:

    def __init__(self, elements):
        self.elements = elements

    def safe_get(self, index):
        try:
            return self.elements[index]
        except IndexError:
            return None
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    accessor = IndexAccessor(sample_list)
    print(accessor.safe_get(2))
    print(accessor.safe_get(5))