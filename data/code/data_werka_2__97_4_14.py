class BinaryCombinator:
    def __init__(self, variable_names=None):
        if variable_names is None:
            variable_names = ['A', 'B']
        if not isinstance(variable_names, (list, tuple)):
            raise ValueError("variable_names must be a list or tuple")
        if len(variable_names) != 2:
            raise ValueError("Expected exactly two binary variables")
        self.vars = list(variable_names)

    def build_table(self):
        header = self.vars[:]
        rows = []
        count = 1 << len(self.vars)
        for i in range(count):
            row = []
            temp = i
            for j in range(len(self.vars) - 1, -1, -1):
                row.append(temp & 1)
                temp >>= 1
            rows.append(row)
        return (header, rows)

if __name__ == '__main__':
    combinator = BinaryCombinator(['X', 'Y'])
    header, table_data = combinator.build_table()
    print(header)
    print(table_data)