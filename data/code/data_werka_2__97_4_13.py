class TruthTableBuilder:
    VARS = ['A', 'B']
    LOOKUP = {
        0: 'False',
        1: 'True'
    }

    def __init__(self, num_vars=2):
        if not isinstance(num_vars, int) or num_vars <= 0:
            raise ValueError("num_vars must be a positive integer")
        self.num_vars = num_vars

    def build(self):
        rows = []
        limit = 1 << self.num_vars
        for i in range(limit):
            row = []
            for var_name in self.VARS[:self.num_vars]:
                col_idx = self.VARS.index(var_name)
                bit = (i >> (self.num_vars - 1 - col_idx)) & 1
                row.append(self.LOOKUP[bit])
            rows.append(row)
        return rows

if __name__ == '__main__':
    builder = TruthTableBuilder(2)
    table = builder.build()
    for row in table:
        print(row)