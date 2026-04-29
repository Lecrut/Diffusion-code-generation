class DynamicListManager:
    def __init__(self):
        self.list = []

    def add_element(self, value: int) -> None:
        self.list.append(value)

    def get_list(self) -> list:
        return self.list

if __name__ == '__main__':
    manager = DynamicListManager()
    value1 = 10
    value2 = 20
    value3 = 30

    manager.add_element(value1)
    manager.add_element(value2)
    manager.add_element(value3)

    result = manager.get_list()
    total = len(result)

    print(result)
    print(total)