class ListContainer:
    def __init__(self, elements):
        self.elements = elements

    @classmethod
    def get_last_element(cls, instance):
        if not instance.elements:
            return None
        return instance.elements[-1]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    container = ListContainer(sample_list)
    last_element = ListContainer.get_last_element(container)
    print(last_element)