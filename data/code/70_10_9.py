class ListChecker:
    def __init__(self, initial_list=None):
        if initial_list is None:
            initial_list = []
        self.internal_list = initial_list

    def get_first_and_last(self):
        if not self.internal_list:
            raise ValueError("List is empty")
        return self.internal_list[0], self.internal_list[-1]

if __name__ == '__main__':
    checker = ListChecker([1, 2, 3, 4, 5])
    first, last = checker.get_first_and_last()
    print(f"First item: {first}")
    print(f"Last item: {last}")