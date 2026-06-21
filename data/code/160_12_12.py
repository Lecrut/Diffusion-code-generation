item_names = ('apple', 'banana', 'cherry')

class ItemChecker:
    def __init__(self, names):
        self.names = names

    def item_exists(self, item):
        return item in self.names

if __name__ == '__main__':
    checker = ItemChecker(item_names)
    print(f"Item 'apple' exists: {checker.item_exists('apple')}")
    print(f"Item 'grape' exists: {checker.item_exists('grape')}")