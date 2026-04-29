class DynamicListManager:
    def __init__(self):
        self._data = []

    def add_element(self, element: object) -> None:
        self._data.append(element)

    def get_data(self) -> list:
        return self._data

def manager_add_and_get(initial_list: list, elements_to_add: list) -> list:
    manager = DynamicListManager()
    for element in initial_list:
        manager.add_element(element)
    for element in elements_to_add:
        manager.add_element(element)
    return manager.get_data()

if __name__ == '__main__':
    initial_data = [1, 2, 3]
    new_data = [4, 5, 6]
    result = manager_add_and_get(initial_data, new_data)
    print(result)