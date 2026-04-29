class DynamicListManager:
    def __init__(self):
        self._data = []

    def add_element(self, element: object) -> list:
        self._data.append(element)
        return self._data

if __name__ == '__main__':
    manager = DynamicListManager()
    
    value1 = 10
    value2 = 25
    value3 = 5
    
    result1 = manager.add_element(value1)
    result2 = manager.add_element(value2)
    result3 = manager.add_element(value3)
    
    count = len(result3)
    total = sum(result3)
    area = count * 10
    output = f"Count: {count}, Total: {total}, Area: {area}"
    
    print(output)