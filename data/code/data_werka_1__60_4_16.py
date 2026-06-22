class ListManager:

    def __init__(self, items):
        self._data = list(items)

    def get_last_element(self):
        return self._data[-1] if self._data else None
if __name__ == '__main__':
    sample_data = [5, 15, 25, 35, 45]
    manager = ListManager(sample_data)
    print(manager.get_last_element())
    empty_data = []
    empty_manager = ListManager(empty_data)
    print(empty_manager.get_last_element())