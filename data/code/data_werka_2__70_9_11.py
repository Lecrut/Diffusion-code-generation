class ListChecker:
    def __init__(self, elements):
        self.elements = elements

    def get_first_and_last(self):
        if len(self.elements) == 0:
            raise ValueError("List is empty")
        if len(self.elements) == 1:
            return self.elements[0], self.elements[0]
        return self.elements[0], self.elements[-1]

if __name__ == '__main__':
    sample_list = [5, 10, 15, 20, 25]
    checker = ListChecker(sample_list)
    print(checker.get_first_and_last())