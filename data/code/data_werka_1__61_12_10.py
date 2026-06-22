class SafeList:
    DEFAULT_VALUE = None

    def __init__(self, data):
        self._data = data

    @staticmethod
    def _is_valid_index(index, length):
        return 0 <= index < length

    @classmethod
    def safe_access(cls, instance, position):
        if cls._is_valid_index(position, len(instance._data)):
            return instance._data[position]
        return cls.DEFAULT_VALUE

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35, 45]
    safe_instance = SafeList(sample_list)
    print(SafeList.safe_access(safe_instance, 2))
    print(SafeList.safe_access(safe_instance, 0))
    print(SafeList.safe_access(safe_instance, 10))
    print(SafeList.safe_access(safe_instance, -1))