class ListChecker:
    def __init__(self, data):
        self.data = data

    def get_first_and_last(self):
        if not self.data:
            return None, None
        return self.data[0], self.data[-1]

if __name__ == '__main__':
    checker = ListChecker([1, 2, 3, 4, 5])
    first, last = checker.get_first_and_last()
    print(f"First: {first}, Last: {last}")