class DynamicListManager:
    def __init__(self):
        self.data = []

    def add_element(self, value: int) -> None:
        self.data.append(value)

    def get_list(self) -> list:
        return self.data

if __name__ == '__main__':
    manager = DynamicListManager()
    initial_value = 10
    value_to_add_1 = 20
    value_to_add_2 = 30

    manager.add_element(initial_value)
    manager.add_element(value_to_add_1)
    manager.add_element(value_to_add_2)

    result = manager.get_list()
    count = len(result)
    total = sum(result)

    print(result)
    print(count)
    print(total)