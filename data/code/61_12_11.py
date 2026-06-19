class SafeListHandler:
    def __init__(self, list_data):
        self._list_data = list_data

    @classmethod
    def get_safe_element(cls, instance, idx):
        if 0 <= idx < len(instance._list_data):
            return instance._list_data[idx]
        return None

if __name__ == '__main__':
    SAMPLE_LIST = [10, 20, 30, 40, 50]
    handler = SafeListHandler(SAMPLE_LIST)
    print(SafeListHandler.get_safe_element(handler, 2))
    print(SafeListHandler.get_safe_element(handler, 0))
    print(SafeListHandler.get_safe_element(handler, 5))
    print(SafeListHandler.get_safe_element(handler, -1))