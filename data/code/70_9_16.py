class ListChecker:
    def __init__(self, values):
        self._values = list(values)

    def get_first_and_last(self):
        if len(self._values) == 0:
            raise ValueError("List is empty")
        return self._values[0], self._values[-1]

    def get_count(self):
        return len(self._values)

if __name__ == '__main__':
    sample_list = [5, 10, 15, 20, 25]
    checker = ListChecker(sample_list)
    first, last = checker.get_first_and_last()
    print(first)
    print(last)
    print(checker.get_count())