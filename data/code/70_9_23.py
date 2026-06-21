class ListChecker:
    _STATUS_MAP = {
        0: "empty",
        1: "single",
        2: "pair",
        3: "triple",
        4: "quadruple",
        5: "quintuple",
        6: "sextuple",
        7: "septuple",
        8: "octuple",
        9: "nonuple",
        10: "decuple"
    }

    def __init__(self, source_list):
        self._elements = list(source_list)

    def get_first_and_last(self):
        length = len(self._elements)
        if length == 0:
            raise ValueError("List is empty")
        if length == 1:
            val = self._elements[0]
            return (val, val)
        return (self._elements[0], self._elements[-1])

    def get_status(self):
        length = len(self._elements)
        if length in self._STATUS_MAP:
            return self._STATUS_MAP[length]
        return f"size_{length}"

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    checker = ListChecker(sample_values)
    first, last = checker.get_first_and_last()
    status = checker.get_status()
    print(f"First: {first}, Last: {last}, Status: {status}")