item_names = ('apple', 'banana', 'cherry')

class ItemChecker:
    ITEMS = item_names

    @staticmethod
    def item_exists(item):
        return item in ItemChecker.ITEMS

if __name__ == '__main__':
    checker = ItemChecker()
    print(f"Item 'banana' exists: {checker.item_exists('banana')}")
    print(f"Item 'grape' exists: {checker.item_exists('grape')}")