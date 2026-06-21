class ListChecker:
    MAX_RETRIES = 3
    DEFAULT_EMPTY_MSG = "Sequence must contain at least one element"

    def __init__(self, empty_message=None):
        self.empty_message = empty_message if empty_message else self.DEFAULT_EMPTY_MSG

    def get_extremes(self, sequence):
        if not sequence:
            raise ValueError(self.empty_message)
        first = sequence[0]
        last = sequence[-1]
        return (first, last)

if __name__ == '__main__':
    data = [5, 15, 25, 35, 45]
    checker = ListChecker()
    result = checker.get_extremes(data)
    print(result)