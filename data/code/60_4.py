class ListUtils:
    def __init__(self, data):
        self._internal_list = list(data)
    def get_last_element(self):
        if not self._internal_list:
            return None
        return self._internal_list[-1]
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    utils = ListUtils(sample_data)
    last_element = utils.get_last_element()
    print(last_element)
    sample_data_empty = []
    utils_empty = ListUtils(sample_data_empty)
    last_element_empty = utils_empty.get_last_element()
    print(last_element_empty)