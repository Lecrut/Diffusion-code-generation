class BooleanLogicTable:
    def __init__(self, val_a, val_b):
        self.a = val_a
        self.b = val_b
        self._cache = {}

    def _compute(self, key, func):
        if key not in self._cache:
            self._cache[key] = func(self.a, self.b)
        return self._cache[key]

    def get_table(self):
        table = {
            "input_a": self.a,
            "input_b": self.b,
            "a AND b": lambda x, y: x and y,
            "a OR b": lambda x, y: x or y,
            "a XOR b": lambda x, y: x != y,
            "a NAND b": lambda x, y: not (x and y),
            "a NOR b": lambda x, y: not (x or y),
            "a IMPLIES b": lambda x, y: (not x) or y,
            "b IMPLIES a": lambda x, y: (not y) or x,
            "a XNOR b": lambda x, y: x == y,
            "NOT a": lambda x, y: not x,
            "NOT b": lambda x, y: not y,
        }
        result = {}
        for label, op in table.items():
            if label.startswith("input"):
                result[label] = table[label]
            else:
                result[label] = op(self.a, self.b)
        return result

    def get_and_result(self):
        return self.a and self.b

    def get_or_result(self):
        return self.a or self.b

if __name__ == '__main__':
    logic = BooleanLogicTable(True, False)
    print(logic.get_table())
    print(logic.get_and_result())
    print(logic.get_or_result())