class BinaryCombinator:
    def __init__(self, var_names=None):
        if var_names is None:
            var_names = ['A', 'B']
        self.var_names = var_names
        self.count = len(var_names)
        self._cache = {}

    def _get_combinations(self):
        if self.count not in self._cache:
            self._cache[self.count] = []
            limit = 1 << self.count
            for i in range(limit):
                combo = []
                for j in range(self.count):
                    bit = (i >> (self.count - 1 - j)) & 1
                    combo.append(bit)
                self._cache[self.count].append(combo)
        return self._cache[self.count]

    def generate_table(self):
        combinations = self._get_combinations()
        header = self.var_names
        rows = [header]
        for combo in combinations:
            rows.append(combo)
        return rows

    def get_variable_names(self):
        return list(self.var_names)

if __name__ == '__main__':
    combinator = BinaryCombinator(['X', 'Y'])
    table = combinator.generate_table()
    print(table)
    print(combinator.get_variable_names())