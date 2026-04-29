class DynamicListManager:
    def __init__(self):
        self._list = []

    def add_element(self, value: int) -> int:
        self._list.append(value)
        count = len(self._list)
        return count

    def get_list(self) -> list:
        return self._list

if __name__ == '__main__':
    manager = DynamicListManager()
    
    value1 = 10
    value2 = 20
    value3 = 30
    
    count1 = manager.add_element(value1)
    count2 = manager.add_element(value2)
    count3 = manager.add_element(value3)
    
    total = count3
    result = manager.get_list()
    
    print(total)
    print(result)