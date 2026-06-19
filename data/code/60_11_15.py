class ListAccessor:
    def __init__(self, elements):
        self.elements = elements
    def get_last_element(self):
        return self.elements[-1]

if __name__ == '__main__':
    sample_elements = ['red', 'green', 'blue']
    accessor = ListAccessor(sample_elements)
    last_color = accessor.get_last_element()
    print(last_color)