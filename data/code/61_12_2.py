class SafeListManager:

    def __init__(self, items):
        self._items = items

    @classmethod
    def access_item(cls, instance, index):
        if 0 <= index < len(instance._items):
            return instance._items[index]
        return None
if __name__ == '__main__':
    sample_data = [100, 200, 300, 400, 500]
    manager = SafeListManager(sample_data)
    print(SafeListManager.access_item(manager, 1))
    print(SafeListManager.access_item(manager, -1))
    print(SafeListManager.access_item(manager, 5))
    print(SafeListManager.access_item(manager, 2))