class ListChecker:
    def __init__(self, elements):
        self.elements = elements

    def check_first_last(self):
        if len(self.elements) < 2:
            raise ValueError("List must contain at least two elements")
        return self.elements[0], self.elements[-1]

if __name__ == '__main__':
    checker = ListChecker([1, 2, 3, 4, 5])
    print(checker.check_first_last())