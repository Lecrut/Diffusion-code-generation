class ListProcessor:
    DEFAULT_LIST = [10, 20, 30, 40, 50]

    def __init__(self, data=None):
        self._internal_list = list(data) if data is not None else self.DEFAULT_LIST

    @classmethod
    def get_last_element(cls, instance):
        if not instance._internal_list:
            return None
        return instance._internal_list[-1]

if __name__ == '__main__':
    sample_data = [5, 15, 25, 35, 45]
    processor = ListProcessor(sample_data)
    last_element = ListProcessor.get_last_element(processor)
    print(last_element)

    empty_processor = ListProcessor()
    last_element_empty = ListProcessor.get_last_element(empty_processor)
    print(last_element_empty)