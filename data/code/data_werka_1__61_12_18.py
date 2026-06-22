class SafeListHandler:
    def __init__(self, data):
        self._data = data

    @classmethod
    def safe_retrieve(cls, instance, index):
        if 0 <= index < len(instance._data):
            return instance._data[index]
        return None

if __name__ == '__main__':
    sample_values = [5, 15, 25, 35, 45]
    handler = SafeListHandler(sample_values)
    print(SafeListHandler.safe_retrieve(handler, 3))
    print(SafeListHandler.safe_retrieve(handler, -1))
    print(SafeListHandler.safe_retrieve(handler, 5))
    print(SafeListHandler.safe_retrieve(handler, 0))