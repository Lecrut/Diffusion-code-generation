class CustomListWrapper:

    def __init__(self, elements):
        self.elements = elements

    @property
    def first(self):
        if not self.elements:
            raise IndexError('The list is empty')
        return self.elements[0]
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    wrapper = CustomListWrapper(sample_list)
    print(wrapper.first)