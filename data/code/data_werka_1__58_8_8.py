class CustomListWrapper:
    def __init__(self, elements):
        self.elements = elements

    @property
    def first(self):
        if not self.elements:
            raise IndexError('The list is empty')
        return self.elements[0]

if __name__ == '__main__':
    sample_values = [7, 17, 27, 37, 47]
    wrapper_object = CustomListWrapper(sample_values)
    
    try:
        first_element_value = wrapper_object.first
        print(f"The first element is: {first_element_value}")
    except IndexError as e:
        print(e)