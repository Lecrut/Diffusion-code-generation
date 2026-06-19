class SafeList:
    def __init__(self, data):
        self._data = data

    @classmethod
    def safe_get(cls, instance, index):
        return instance._data[index] if 0 <= index < len(instance._data) else None

if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5]
    safe_list_instance = SafeList(sample_data)
    print(SafeList.safe_get(safe_list_instance, 2))
    print(SafeList.safe_get(safe_list_instance, -1))
    print(SafeList.safe_get(safe_list_instance, 5))