class MutableListManager:
    def __init__(self, initial_list):
        self._data = list(initial_list)
    def remove_by_index(self, index):
        if not (0 <= index < len(self._data)):
            raise IndexError("Index out of bounds")
        self._data.pop(index)
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    manager = MutableListManager(sample_list)
    print("Initial list:", sample_list)
    try:
        manager.remove_by_index(2)
        print("After removing index 2:", manager._data)
        manager.remove_by_index(0)
        print("After removing index 0:", manager._data)
    except IndexError as e:
        print("Error caught:", e)
    try:
        manager.remove_by_index(5)
    except IndexError as e:
        print("Error caught for out-of-bounds index:", e)
    try:
        manager.remove_by_index(-1)
    except IndexError as e:
        print("Error caught for negative index:", e)