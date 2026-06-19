class CustomListWrapper:
    def __init__(self, elements):
        self.elements = elements

    @property
    def first(self):
        if not self.elements:
            raise ValueError('The list is empty')
        return self._get_first_element()

    def _get_first_element(self):
        return self.elements[0]

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    wrapper_instance = CustomListWrapper(sample_values)
    
    try:
        first_item = wrapper_instance.first
        print(f"The first element is: {first_item}")
    except ValueError as e:
        print(e)