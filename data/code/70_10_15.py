class ListChecker:
    def __init__(self, data):
        self.data = data

    def get_first_and_last(self):
        if not self.data:
            return None, None
        return self.data[0], self.data[-1]

if __name__ == '__main__':
    checker = ListChecker([10, 20, 30, 40, 50])
    first, last = checker.get_first_and_last()
    print(f"First item: {first}")
    print(f"Last item: {last}")