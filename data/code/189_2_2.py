class MutableListManager:
    def __init__(self, initial_list):
        self._data = list(initial_list)
    def remove_by_index(self, index):
        n = len(self._data)
        if not (0 <= index < n):
            raise IndexError("Index out of bounds")
        del self._data[index]
if __name__ == '__main__':
    initial_list = [10, 20, 30, 40, 50]
    manager = MutableListManager(initial_list)
    print("Initial list:", manager._data)
    try:
        manager.remove_by_index(2)
        print("After removing index 2:", manager._data)
        manager.remove_by_index(0)
        print("After removing index 0:", manager._data)
        manager.remove_by_index(100)
    except IndexError as e:
        print("Caught error:", e)
        print("List remains:", manager._data)