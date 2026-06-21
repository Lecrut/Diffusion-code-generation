item_names = ('apple', 'banana', 'cherry')

class ItemChecker:
    def __init__(self, items):
        self.items = items

    def item_exists(self, item):
        return item in self.items

if __name__ == '__main__':
    checker = ItemChecker(item_names)
    print(checker.item_exists('banana'))
    print(checker.item_exists('grape'))