class ListChecker:
    _EMPTY_MSG = "List cannot be empty"

    @staticmethod
    def _validate_sequence(seq):
        if not seq:
            raise ValueError(ListChecker._EMPTY_MSG)
        return seq

    def get_extremes(self, data):
        validated = self._validate_sequence(data)
        first = validated[0]
        last = validated[-1]
        return (first, last)

if __name__ == '__main__':
    items = [5, 15, 25, 35, 45]
    checker = ListChecker()
    print(checker.get_extremes(items))