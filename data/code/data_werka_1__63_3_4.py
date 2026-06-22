class ListContainer:
    def __init__(self, elements):
        self.elements = elements

    @classmethod
    def get_first_element(cls, instance):
        if instance.elements:
            return instance.elements[0]
        return None

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    container = ListContainer(sample_list)
    first_element = ListContainer.get_first_element(container)
    print(first_element)