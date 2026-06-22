class ListContainer:
    def __init__(self, elements):
        self._elements = elements

    @classmethod
    def get_second_element(cls, instance):
        return instance._elements[1]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    container = ListContainer(sample_list)
    print(ListContainer.get_second_element(container))