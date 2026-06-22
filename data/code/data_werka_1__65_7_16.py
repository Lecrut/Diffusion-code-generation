class SafeList:

    def __init__(self, data):
        self._data = data

    def get_element(self, index):
        if not isinstance(index, int) or index < 0 or index >= len(self._data):
            raise IndexError('Index out of range')
        return self._data[index]
if __name__ == '__main__':
    sample_data = [100, 200, 300, 400, 500]
    safe_list = SafeList(sample_data)
    try:
        print(safe_list.get_element(0))
        print(safe_list.get_element(2))
        print(safe_list.get_element(4))
        print(safe_list.get_element(5))
    except IndexError as e:
        print(e)