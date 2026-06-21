class ItemChecker:
    def __init__(self):
        self.item_names = ('apple', 'banana', 'cherry')

    def item_exists(self, item):
        return item in self.item_names

if __name__ == '__main__':
    checker = ItemChecker()
    print(f"Item 'banana' exists: {checker.item_exists('banana')}")
    print(f"Item 'grape' exists: {checker.item_exists('grape')}")