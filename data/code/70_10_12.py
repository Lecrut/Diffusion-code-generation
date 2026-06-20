class ListChecker:
    def __init__(self, items):
        self.items = items

    def get_first_and_last(self):
        if not self.items:
            raise ValueError("List is empty")
        return self.items[0], self.items[-1]

if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'cherry']
    checker = ListChecker(sample_items)
    first, last = checker.get_first_and_last()
    print(f"First item: {first}")
    print(f"Last item: {last}")