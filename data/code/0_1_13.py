class DynamicListManager:
    def __init__(self):
        self.data = []

    def add_element(self, value: object) -> None:
        self.data.append(value)

    def get_list(self) -> list:
        return self.data

if __name__ == '__main__':
    manager = DynamicListManager()
    
    initial_value = 10
    manager.add_element(initial_value)
    
    second_value = 25
    manager.add_element(second_value)
    
    third_value = 33
    manager.add_element(third_value)
    
    result = manager.get_list()
    count = len(result)
    total = sum(result)
    
    print(f"value: {initial_value}")
    print(f"value: {second_value}")
    print(f"value: {third_value}")
    print(f"count: {count}")
    print(f"total: {total}")
    print(f"result: {result}")