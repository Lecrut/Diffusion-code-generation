class ListProcessor:
    def __init__(self, data):
        self._internal_list = list(data)

    @classmethod
    def get_last_element(cls, instance):
        if not instance._internal_list:
            return None
        return instance._internal_list[-1]

if __name__ == '__main__':
    SAMPLE_DATA = [5, 15, 25, 35, 45]
    processor = ListProcessor(SAMPLE_DATA)
    last_element = ListProcessor.get_last_element(processor)
    print(last_element)

    EMPTY_SAMPLE_DATA = []
    empty_processor = ListProcessor(EMPTY_SAMPLE_DATA)
    last_element_empty = ListProcessor.get_last_element(empty_processor)
    print(last_element_empty)