class ListProcessor:
    def __init__(self, data):
        self._internal_list = list(data)

    @classmethod
    def from_dict(cls, data_dict):
        return cls(data_dict.get('list', []))

    def get_last_element(self):
        if not self._internal_list:
            return None
        return self._internal_list[-1]

if __name__ == '__main__':
    sample_data = {'list': [10, 20, 30, 40, 50]}
    processor = ListProcessor.from_dict(sample_data)
    last_element = processor.get_last_element()
    print(last_element)

    sample_data_empty = {'list': []}
    processor_empty = ListProcessor.from_dict(sample_data_empty)
    last_element_empty = processor_empty.get_last_element()
    print(last_element_empty)