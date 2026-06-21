class StringListChecker:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def _is_empty(lst):
        return len(lst) == 0

    def has_item(self, item):
        if self._is_empty(self.data):
            return False
        return item in self.data

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry']
    checker = StringListChecker(sample_list)
    item1 = 'banana'
    result1 = checker.has_item(item1)
    print(f"Does '{item1}' exist in the list? {result1}")
    item2 = 'grape'
    result2 = checker.has_item(item2)
    print(f"Does '{item2}' exist in the list? {result2}")
    item3 = 'apple'
    result3 = checker.has_item(item3)
    print(f"Does '{item3}' exist in the list? {result3}")