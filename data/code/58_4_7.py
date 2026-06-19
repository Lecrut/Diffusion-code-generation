class ListProcessor:
    def __init__(self, data):
        self.data = data

    @classmethod
    def from_dict(cls, data_dict):
        return cls(list(data_dict.values()))

    def get_first_element(self):
        return self.data[0] if self.data else None

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35]
    processor = ListProcessor(sample_list)
    first_element = processor.get_first_element()
    print(first_element)

    sample_dict = {'x': 'one', 'y': 'two', 'z': 'three'}
    dict_processor = ListProcessor.from_dict(sample_dict)
    first_element_from_dict = dict_processor.get_first_element()
    print(first_element_from_dict)