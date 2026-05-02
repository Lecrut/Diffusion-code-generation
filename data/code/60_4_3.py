class ListUtility:
    def __init__(self, data):
        self._internal_list = list(data)
    def get_last_element(self):
        if not self._internal_list:
            return None
        return self._internal_list[-1]
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    utility = ListUtility(sample_data)
    last_element = utility.get_last_element()
    print(last_element)
    sample_data_empty = []
    utility_empty = ListUtility(sample_data_empty)
    last_element_empty = utility_empty.get_last_element()
    print(last_element_empty)