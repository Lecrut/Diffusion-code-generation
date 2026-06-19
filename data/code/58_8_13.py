class CustomListWrapper:
    def __init__(self, elements):
        self.elements = elements

    @property
    def first(self):
        if not self.elements:
            return None
        return self.elements[0]

if __name__ == '__main__':
    sample_data = [7, 17, 27, 37, 47]
    wrapper_instance = CustomListWrapper(sample_data)
    print(wrapper_instance.first)