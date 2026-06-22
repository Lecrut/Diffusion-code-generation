class ListChecker:
    _STATUS_MAP = {
        0: "empty",
        1: "single",
        2: "pair",
        3: "multiple"
    }

    def __init__(self, data):
        self._elements = list(data)

    def get_first_and_last(self):
        length = len(self._elements)
        if length == 0:
            raise ValueError("List is empty")
        if length == 1:
            val = self._elements[0]
            return val, val
        return self._elements[0], self._elements[-1]

    def get_status(self):
        length = len(self._elements)
        if length <= 3:
            return self._STATUS_MAP[length]
        return self._STATUS_MAP[3]

if __name__ == '__main__':
    sample_data = [99, 45, 12, 67, 3, 88]
    checker = ListChecker(sample_data)
    result = checker.get_first_and_last()
    status = checker.get_status()
    print(result)
    print(status)