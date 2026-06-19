class CustomListWrapper:
    EMPTY_LIST_ERROR = 'The list is empty'

    def __init__(self, elements):
        self.elements = elements

    @property
    def first(self):
        if not self.elements:
            raise IndexError(self.EMPTY_LIST_ERROR)
        return self.elements[0]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    wrapper = CustomListWrapper(sample_list)
    try:
        print(wrapper.first)
    except IndexError as e:
        print(e)