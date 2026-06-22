class ListChecker:
    def __init__(self, values):
        self._container = list(values)

    def get_first_and_last(self):
        n = len(self._container)
        if n == 0:
            raise ValueError("List is empty")
        if n == 1:
            val = self._container[0]
            return (val, val)
        return (self._container[0], self._container[-1])

if __name__ == '__main__':
    sample_list = [5, 12, 7, 89, 3]
    checker = ListChecker(sample_list)
    print(checker.get_first_and_last())
    single_list = [42]
    checker_single = ListChecker(single_list)
    print(checker_single.get_first_and_last())