class CustomListWrapper:
    def __init__(self, elements):
        self.elements = elements

    @property
    def first_element(self):
        if self.elements:
            return self.elements[0]
        else:
            raise IndexError("The list is empty")

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    wrapper = CustomListWrapper(sample_list)
    print(wrapper.first_element)