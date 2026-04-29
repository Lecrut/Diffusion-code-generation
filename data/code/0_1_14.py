class DynamicListManager:
    def __init__(self):
        self._data = []

    def add_element(self, element: int) -> None:
        self._data.append(element)

    def get_list(self) -> list:
        return self._data

if __name__ == '__main__':
    initial_value = 10
    elements_to_add = [5, 15, 25, 35]

    manager = DynamicListManager()
    total = 0

    for value in elements_to_add:
        manager.add_element(value)
        total += value

    result = manager.get_list()
    count = len(result)

    print(result)
    print(count)
    print(total)