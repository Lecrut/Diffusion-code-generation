class ListChecker:
    def __init__(self, elements):
        self.elements = elements

    def get_first_and_last(self):
        if not self.elements:
            return None, None
        return self.elements[0], self.elements[-1]

if __name__ == '__main__':
    checker = ListChecker([1, 2, 3, 4, 5])
    first, last = checker.get_first_and_last()
    print(f"First: {first}, Last: {last}")