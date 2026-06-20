class ListChecker:
    def __init__(self, lst):
        self.lst = lst

    def get_first_and_last(self):
        if not self.lst:
            return None, None
        return self.lst[0], self.lst[-1]

if __name__ == '__main__':
    checker = ListChecker([1, 2, 3, 4, 5])
    first, last = checker.get_first_and_last()
    print(f"First: {first}, Last: {last}")