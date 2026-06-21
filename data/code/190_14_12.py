class ItemChecker:
    def __init__(self, lst):
        self.item_set = set(lst)

    def contains_item(self, value):
        return value in self.item_set

if __name__ == '__main__':
    checker = ItemChecker([1, 2, 3, 4, 5])
    print(checker.contains_item(3))
    print(checker.contains_item(6))