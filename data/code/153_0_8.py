class ItemChecker:
    def __init__(self, item_list):
        self.item_list = item_list

    def check_existence(self, item):
        return item in self.item_list

if __name__ == '__main__':
    checker = ItemChecker(["banana", "orange", "apple", "grape", "kiwi"])
    print(f"Does 'apple' exist? {checker.check_existence('apple')}")
    print(f"Does 'mango' exist? {checker.check_existence('mango')}")