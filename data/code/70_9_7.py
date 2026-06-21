class ListChecker:
    def __init__(self, sequence):
        self._store = sequence

    def get_first_and_last(self):
        length = len(self._store)
        if length == 0:
            raise ValueError("Sequence is empty")
        if length == 1:
            return self._store[0], self._store[0]
        return self._store[0], self._store[-1]

if __name__ == '__main__':
    data_set = [100, 200, 300, 400, 500]
    checker = ListChecker(data_set)
    print(checker.get_first_and_last())