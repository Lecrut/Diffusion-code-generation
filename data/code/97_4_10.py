class BinaryTruthTable:
    def __init__(self, var_names=None):
        if var_names is not None:
            if len(var_names) != 2:
                raise ValueError("Exactly two variable names required")
            if not all(isinstance(v, str) and v for v in var_names):
                raise ValueError("Variable names must be non-empty strings")
        self.var_names = var_names or ['A', 'B']

    def get_table(self):
        rows = []
        for val_a in (0, 1):
            for val_b in (0, 1):
                row = {
                    self.var_names[0]: val_a,
                    self.var_names[1]: val_b
                }
                rows.append(row)
        return rows

if __name__ == '__main__':
    engine = BinaryTruthTable(['X', 'Y'])
    data = engine.get_table()
    print(data)