class DynamicListManager:
    def __init__(self):
        self.data = []

    def add_element(self, value: object) -> None:
        self.data.append(value)

    def get_list(self) -> list:
        return self.data

if __name__ == '__main__':
    manager = DynamicListManager()
    value1 = 10
    value2 = "text"
    value3 = 3.14

    manager.add_element(value1)
    manager.add_element(value2)
    manager.add_element(value3)

    result = manager.get_list()
    count = len(result)
    total = sum(result) if all(isinstance(x, (int, float)) for x in result) else 0

    print(result)
    print(count)
    print(total)