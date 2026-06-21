class ElementChecker:

    def __init__(self, data):
        self._data = set(data)

    def contains(self, item):
        return item in self._data
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    checker = ElementChecker(sample_list)
    item1 = 3
    item2 = 6
    print(f'Does the list contain {item1}? {checker.contains(item1)}')
    print(f'Does the list contain {item2}? {checker.contains(item2)}')