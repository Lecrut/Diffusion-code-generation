class ListManager:
    def __init__(self):
        self.data = []

    def add_element(self, element):
        self.data.append(element)

    def get_middle_element(self):
        n = len(self.data)
        if n == 0:
            return None
        middle_index = n // 2
        return self.data[middle_index]

if __name__ == '__main__':
    manager1 = ListManager()
    for i in range(1, 6):
        manager1.add_element(i)
    print(manager1.get_middle_element())

    manager2 = ListManager()
    for i in range(10, 40, 10):
        manager2.add_element(i)
    print(manager2.get_middle_element())

    manager3 = ListManager()
    manager3.add_element(50)
    print(manager3.get_middle_element())

    manager4 = ListManager()
    print(manager4.get_middle_element())