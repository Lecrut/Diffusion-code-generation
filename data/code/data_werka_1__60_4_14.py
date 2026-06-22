class ListContainer:
    def __init__(self, data):
        self._internal_list = list(data)

    @classmethod
    def from_dict(cls, data_dict):
        return cls(list(data_dict.values()))

    def get_last_element(self):
        if not self._internal_list:
            return None
        return self._internal_list[-1]

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    container = ListContainer(sample_data)
    last_element = container.get_last_element()
    print(last_element)

    sample_data_empty = []
    container_empty = ListContainer(sample_data_empty)
    last_element_empty = container_empty.get_last_element()
    print(last_element_empty)

    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    dict_container = ListContainer.from_dict(sample_dict)
    last_element_from_dict = dict_container.get_last_element()
    print(last_element_from_dict)