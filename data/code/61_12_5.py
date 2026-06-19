class SafeListHandler:
    DEFAULT_LIST = [10, 20, 30, 40, 50]

    def __init__(self, data=None):
        self._data = data if data is not None else SafeListHandler.DEFAULT_LIST

    @classmethod
    def get_safe_element(cls, instance, index):
        try:
            return instance._data[index]
        except IndexError:
            return None
if __name__ == '__main__':
    custom_list = [100, 200, 300, 400, 500]
    handler_with_custom_list = SafeListHandler(custom_list)
    print(SafeListHandler.get_safe_element(handler_with_custom_list, 2))
    print(SafeListHandler.get_safe_element(handler_with_custom_list, -1))
    print(SafeListHandler.get_safe_element(handler_with_custom_list, 5))
    default_handler = SafeListHandler()
    print(SafeListHandler.get_safe_element(default_handler, 0))
    print(SafeListHandler.get_safe_element(default_handler, 4))
    print(SafeListHandler.get_safe_element(default_handler, 10))