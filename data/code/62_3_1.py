class DataContainer:
    def __init__(self, data):
        self._internal_list = list(data)
    def get_second_element(self):
        if len(self._internal_list) > 1:
            return self._internal_list[1]
        return None
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40]
    container = DataContainer(sample_data)
    result = container.get_second_element()
    print(result)