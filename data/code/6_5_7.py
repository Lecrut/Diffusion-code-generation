class WeightPairDict:
    def __init__(self):
        self._store = {}

    def add_pair(self, id1, id2, w1, w2):
        key = (id1, id2)
        self._store[key] = (w1, w2)

    def get_difference(self, id1, id2):
        key = (id1, id2)
        if key in self._store:
            w1, w2 = self._store[key]
            return w1 - w2
        return None

    def get_absolute_difference(self, id1, id2):
        diff = self.get_difference(id1, id2)
        if diff is not None:
            return abs(diff)
        return None

if __name__ == '__main__':
    w_dict = WeightPairDict()
    w_dict.add_pair(1, 2, 10.5, 5.2)
    w_dict.add_pair(3, 4, 100, 50)
    w_dict.add_pair(5, 6, 1.5, 1.5)

    result_diff = w_dict.get_difference(1, 2)
    print(f"Difference for pair (1, 2): {result_diff}")

    result_abs_diff = w_dict.get_absolute_difference(3, 4)
    print(f"Absolute difference for pair (3, 4): {result_abs_diff}")

    result_none = w_dict.get_difference(10, 20)
    print(f"Difference for pair (10, 20): {result_none}")