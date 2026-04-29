class DynamicListManager:
    MAX_SIZE = 100

    def __init__(self):
        self.data = []

    def add_element(self, value: int) -> bool:
        if len(self.data) < self.MAX_SIZE:
            self.data.append(value)
            return True
        return False

    def get_list(self) -> list:
        return self.data

if __name__ == '__main__':
    manager = DynamicListManager()
    
    value1 = 10
    value2 = 20
    value3 = 30
    
    result1 = manager.add_element(value1)
    result2 = manager.add_element(value2)
    result3 = manager.add_element(value3)
    
    count = len(manager.get_list())
    total = sum(manager.get_list())
    
    print(f"value: {value1}")
    print(f"result: {result1}")
    print(f"count: {count}")
    print(f"total: {total}")
    print(f"list: {manager.get_list()}")