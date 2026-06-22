class ListProcessor:
    def __init__(self, data):
        if not isinstance(data, list):
            raise ValueError("Data must be a list")
        self._internal_list = list(data)

    def get_last_element(self):
        try:
            return self._internal_list[-1]
        except IndexError:
            return None

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    processor = ListProcessor(sample_data)
    last_element = processor.get_last_element()
    print(last_element)

    sample_data_empty = []
    processor_empty = ListProcessor(sample_data_empty)
    last_element_empty = processor_empty.get_last_element()
    print(last_element_empty)