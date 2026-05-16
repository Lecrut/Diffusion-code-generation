class ListHandler:
    def __init__(self, data):
        self._internal_list = list(data)
    def get_last_element(self):
        if not self._internal_list:
            return None
        return self._internal_list[-1]
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    handler = ListHandler(sample_data)
    last_element = handler.get_last_element()
    print(last_element)
    sample_data_empty = []
    handler_empty = ListHandler(sample_data_empty)
    last_element_empty = handler_empty.get_last_element()
    print(last_element_empty)