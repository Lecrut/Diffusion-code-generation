class StringListChecker:
    def __init__(self, data):
        self._data = data

    @staticmethod
    def check_item(data, item):
        return item in data

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry"]
    checker = StringListChecker(sample_list)
    item1 = "banana"
    result1 = checker.check_item(checker._data, item1)
    print(f"Does '{item1}' exist in the list? {result1}")
    item2 = "grape"
    result2 = checker.check_item(checker._data, item2)
    print(f"Does '{item2}' exist in the list? {result2}")