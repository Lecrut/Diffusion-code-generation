class ListManager:
    def __init__(self, data):
        self._internal_list = list(data)
    
    def get_last_element(self):
        if not self._internal_list:
            return None
        return self._internal_list[-1]

if __name__ == '__main__':
    sample_data = [5, 15, 25, 35, 45]
    manager = ListManager(sample_data)
    last_element = manager.get_last_element()
    print(last_element)

    sample_data_empty = []
    manager_empty = ListManager(sample_data_empty)
    last_element_empty = manager_empty.get_last_element()
    print(last_element_empty)