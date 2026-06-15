class ListChecker:
    def __init__(self, data):
        self.data = data
    def has_item(self, item):
        return item in self.data
if __name__ == '__main__':
    sample_list = [1, 5, 2, 8, 3]
    checker = ListChecker(sample_list)
    item1 = 8
    result1 = checker.has_item(item1)
    print(f"Does {item1} exist in the list? {result1}")
    item2 = 9
    result2 = checker.has_item(item2)
    print(f"Does {item2} exist in the list? {result2}")
    item3 = 2
    result3 = checker.has_item(item3)
    print(f"Does {item3} exist in the list? {result3}")