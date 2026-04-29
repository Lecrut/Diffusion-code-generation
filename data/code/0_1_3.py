class DynamicListManager:
    def __init__(self):
        self.data = []

    def add_element(self, value: int) -> None:
        self.data.append(value)

    def get_list(self) -> list:
        return self.data

if __name__ == '__main__':
    manager = DynamicListManager()
    
    value1 = 10
    value2 = 20
    value3 = 30
    
    manager.add_element(value1)
    manager.add_element(value2)
    manager.add_element(value3)
    
    result = manager.get_list()
    count = len(result)
    total = sum(result)
    
    print(result)
    print(count)
    print(total)