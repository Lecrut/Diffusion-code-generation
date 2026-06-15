class ListManager:
    def __init__(self):
        self._data = []
    def remove_element(self, element_to_remove):
        try:
            index = self._data.index(element_to_remove)
            self._data.pop(index)
        except ValueError:
            pass
if __name__ == '__main__':
    manager = ListManager()
    manager._data = [10, 20, 30, 20, 40]
    print("Initial list:", manager._data)
    manager.remove_element(20)
    print("After removing first 20:", manager._data)
    manager.remove_element(30)
    print("After removing 30:", manager._data)
    manager.remove_element(99)
    print("After removing non-existent 99:", manager._data)