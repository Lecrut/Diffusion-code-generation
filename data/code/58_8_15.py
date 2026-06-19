class CustomListWrapper:
    def __init__(self, elements):
        self.elements = elements

    @property
    def first(self):
        EMPTY_LIST_MESSAGE = 'The list is empty'
        if not self.elements:
            raise ValueError(EMPTY_LIST_MESSAGE)
        return self.elements[0]

if __name__ == '__main__':
    SAMPLE_DATA = [7, 17, 27, 37, 47]
    wrapper_instance = CustomListWrapper(SAMPLE_DATA)
    try:
        first_element = wrapper_instance.first
        print(f"The first element is: {first_element}")
    except ValueError as e:
        print(e)