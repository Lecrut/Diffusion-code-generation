class DynamicListManager:
    def __init__(self):
        self.data = []

    def add_element(self, value: int) -> int:
        self.data.append(value)
        result = len(self.data)
        return result

if __name__ == '__main__':
    manager = DynamicListManager()
    value1 = 10
    value2 = 25
    value3 = 5

    count1 = manager.add_element(value1)
    count2 = manager.add_element(value2)
    count3 = manager.add_element(value3)

    total = count3
    output = manager.data

    print(output)
    print(total)