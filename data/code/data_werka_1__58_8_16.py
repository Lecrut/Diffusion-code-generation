class CustomListWrapper:
    def __init__(self, elements):
        self.elements = elements

    @property
    def first(self):
        if len(self.elements) == 0:
            raise IndexError("The list is empty")
        return self.elements[0]

if __name__ == '__main__':
    example_list = [5, 15, 25, 35, 45]
    wrapper = CustomListWrapper(example_list)
    
    try:
        first_element = wrapper.first
        print(f"The first element is: {first_element}")
    except IndexError as e:
        print(e)