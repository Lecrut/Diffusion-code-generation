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
    value_2 = 20
    value_3 = 30
    
    manager.add_element(value_1)
    manager.add_element(value_2)
    manager.add_element(value_3)
    
    result = manager.get_list()
    count = len(result)
    total = sum(result)
    
    print(f"value: {value_1}")
    print(f"value: {value_2}")
    print(f"value: {value_3}")
    print(f"count: {count}")
    print(f"total: {total}")
    print(f"result: {result}")