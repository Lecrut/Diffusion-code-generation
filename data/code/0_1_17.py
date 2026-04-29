class DynamicListManager:
    def __init__(self):
        self.data = []

    def add_element(self, value: int) -> int:
        self.data.append(value)
        count = len(self.data)
        return count

    def get_list(self) -> list:
        return self.data

if __name__ == '__main__':
    manager = DynamicListManager()
    value1 = 10
    value2 = 20
    value3 = 30

    count1 = manager.add_element(value1)
    count2 = manager.add_element(value2)
    count3 = manager.add_element(value3)

    total = count3
    output = manager.get_list()

    print(total)
    print(output)