class ListValidator:
    def __init__(self, data):
        self._data = list(data)
    
    def validate(self, item):
        return item in self._data

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    validator = ListValidator(sample_list)
    item1 = 3
    item2 = 6
    print(f"Does the list contain {item1}? {validator.validate(item1)}")
    print(f"Does the list contain {item2}? {validator.validate(item2)}")