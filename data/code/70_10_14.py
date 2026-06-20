class ListChecker:
    def __init__(self, items):
        self.items = items

    def get_first_and_last(self):
        if not self.items:
            raise ValueError("List is empty")
        return self.items[0], self.items[-1]

if __name__ == '__main__':
    checker = ListChecker([1, 2, 3, 4, 5])
    first, last = checker.get_first_and_last()
    print(f"First: {first}, Last: {last}")