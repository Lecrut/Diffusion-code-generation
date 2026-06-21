class StringChecker:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def check_item(data, item):
        return item in data

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry"]
    checker = StringChecker(sample_list)
    item1 = "banana"
    result1 = checker.check_item(checker.data, item1)
    print(f"Does {item1} exist in the list? {result1}")
    item2 = "grape"
    result2 = checker.check_item(checker.data, item2)
    print(f"Does {item2} exist in the list? {result2}")