class CustomListWrapper:
    def __init__(self, elements):
        self.elements = elements

    @property
    def first(self):
        if not self.elements:
            raise ValueError('The list is empty')
        return self.elements[0]

if __name__ == '__main__':
    sample_data = [5, 15, 25, 35, 45]
    wrapper_instance = CustomListWrapper(sample_data)
    try:
        first_element = wrapper_instance.first
        print(f"The first element is: {first_element}")
    except ValueError as e:
        print(e)