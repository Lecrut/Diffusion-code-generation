class ListChecker:
    def __init__(self, lst):
        self.lst = lst

    def get_first_and_last(self):
        if not self.lst:
            return None
        return self.lst[0], self.lst[-1]

if __name__ == '__main__':
    checker = ListChecker([1, 2, 3, 4, 5])
    print(checker.get_first_and_last())