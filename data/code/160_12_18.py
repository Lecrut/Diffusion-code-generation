ITEM_NAMES = ('apple', 'banana', 'cherry')

class ItemChecker:
    @staticmethod
    def item_exists(item):
        return item in ITEM_NAMES

if __name__ == '__main__':
    sample_item1 = 'banana'
    sample_item2 = 'grape'
    print(f"Item '{sample_item1}' exists: {ItemChecker.item_exists(sample_item1)}")
    print(f"Item '{sample_item2}' exists: {ItemChecker.item_exists(sample_item2)}")