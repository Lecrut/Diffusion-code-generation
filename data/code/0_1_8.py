class DynamicListManager:
    def __init__(self):
        self.data = []

    def add_element(self, element: int) -> None:
        self.data.append(element)

    def get_list(self) -> list:
        return self.data

if __name__ == '__main__':
    manager = DynamicListManager()
    value_1 = 10
    value_2 = 25
    value_3 = 5

    manager.add_element(value_1)
    manager.add_element(value_2)
    manager.add_element(value_3)

    result = manager.get_list()
    count = len(result)
    total = sum(result)

    print(result)
    print(count)
    print(total)