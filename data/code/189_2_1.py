class MutableListManager:
    def __init__(self, initial_list):
        self._data = list(initial_list)
    def remove_by_index(self, index):
        if not (0 <= index < len(self._data)):
            raise IndexError("Index out of bounds")
        del self._data[index]
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    manager = MutableListManager(sample_list)
    print("Initial list:", manager._data)
    try:
        manager.remove_by_index(2)
        print("After removing index 2:", manager._data)
        manager.remove_by_index(0)
        print("After removing index 0:", manager._data)
        manager.remove_by_index(10)
    except IndexError as e:
        print("Error caught:", e)
    try:
        manager.remove_by_index(5)
    except IndexError as e:
        print("Error caught:", e)