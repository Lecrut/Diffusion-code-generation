class SafeListHandler:
    def __init__(self, data):
        self._data = data

    @classmethod
    def get_safe_element(cls, instance, index):
        if not isinstance(instance, cls) or not isinstance(index, int):
            return None
        try:
            return instance._data[index]
        except IndexError:
            return None

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    handler = SafeListHandler(sample_list)
    print(SafeListHandler.get_safe_element(handler, 2))
    print(SafeListHandler.get_safe_element(handler, 0))
    print(SafeListHandler.get_safe_element(handler, 5))
    print(SafeListHandler.get_safe_element(handler, -1))