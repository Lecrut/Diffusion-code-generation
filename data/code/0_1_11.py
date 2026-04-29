class DynamicListManager:
    def __init__(self):
        self.data = []

    def add_element(self, element: int) -> int:
        self.data.append(element)
        result = len(self.data)
        return result

    def get_list(self) -> list:
        return self.data

if __name__ == '__main__':
    manager = DynamicListManager()
    value_one = 10
    value_two = 20
    value_three = 30

    count_one = manager.add_element(value_one)
    count_two = manager.add_element(value_two)
    count_three = manager.add_element(value_three)

    total = count_three
    output = manager.get_list()

    print(total)
    print(output)