class CustomListWrapper:
    def __init__(self, elements):
        self.elements = elements

    @property
    def first(self):
        if len(self.elements) == 0:
            raise IndexError("The list is empty")
        return self.elements[0]

if __name__ == '__main__':
    test_data = [1, 2, 3, 4, 5]
    wrapper_object = CustomListWrapper(test_data)
    try:
        initial_element = wrapper_object.first
        print(initial_element)
    except IndexError as e:
        print(e)