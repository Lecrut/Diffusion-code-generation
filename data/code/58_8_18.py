class CustomListWrapper:
    EMPTY_LIST_MESSAGE = 'The list is empty'

    def __init__(self, elements):
        self.elements = elements

    @property
    def first(self):
        if not self.elements:
            raise IndexError(CustomListWrapper.EMPTY_LIST_MESSAGE)
        return self.elements[0]

if __name__ == '__main__':
    sample_data = [7, 17, 27, 37, 47]
    wrapper_instance = CustomListWrapper(sample_data)
    try:
        first_element = wrapper_instance.first
        print(f"The first element is: {first_element}")
    except IndexError as e:
        print(e)