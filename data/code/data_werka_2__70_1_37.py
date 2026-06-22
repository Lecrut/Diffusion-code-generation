class ListChecker:
    _empty_msg = "Cannot retrieve extremes from an empty sequence"
    _type_map = {
        "list": list,
        "tuple": tuple,
        "range": range
    }

    def get_extremes(self, sequence):
        if not isinstance(sequence, (list, tuple, range)):
            raise ValueError("Input must be a sequence type")
        if len(sequence) == 0:
            raise ValueError(self._empty_msg)
        first = sequence[0]
        last = sequence[-1]
        return (first, last)

if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]
    checker = ListChecker()
    extremes = checker.get_extremes(data)
    print(extremes)