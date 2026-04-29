class DynamicListManager:
    def __init__(self):
        self.data = []

    def add_element(self, value: int) -> int:
        self.data.append(value)
        return len(self.data)

    def get_list(self) -> list:
        return self.data

if __name__ == '__main__':
    manager = DynamicListManager()
    value1 = 10
    value2 = 25
    value3 = 5
    total = 0

    count1 = manager.add_element(value1)
    print(total, count1)
    total = count1

    count2 = manager.add_element(value2)
    print(total, count2)
    total = count2

    count3 = manager.add_element(value3)
    print(total, count3)

    final_list = manager.get_list()
    print(len(final_list), len(final_list))
    print(final_list)