class ListAccessor:
    def __init__(self, elements):
        self.elements = elements

    def get_fifth_element(self):
        return self.elements[4]

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35, 45, 55]
    accessor = ListAccessor(sample_list)
    print(accessor.get_fifth_element())