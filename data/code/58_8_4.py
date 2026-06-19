class CustomListWrapper:
    def __init__(self, elements):
        self.elements = elements

    @property
    def first(self):
        if not self.elements:
            return None
        return self.elements[0]

if __name__ == '__main__':
    sample_list = [100, 200, 300, 400, 500]
    wrapper = CustomListWrapper(sample_list)
    print(wrapper.first)