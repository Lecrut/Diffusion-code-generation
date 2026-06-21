class BinaryVariableTableBuilder:
    def __init__(self, variable_names=None):
        if variable_names is None:
            variable_names = ['A', 'B']
        elif len(variable_names) != 2:
            raise ValueError("Exactly two variable names are required")
        self.variables = variable_names
        self.table = []
        self._build_table()

    def _build_table(self):
        values = [0, 1]
        for v1 in values:
            for v2 in values:
                self.table.append({
                    self.variables[0]: v1,
                    self.variables[1]: v2
                })

    def get_rows(self):
        return self.table

def main():
    builder = BinaryVariableTableBuilder(['X', 'Y'])
    rows = builder.get_rows()
    for row in rows:
        print(row)

if __name__ == '__main__':
    main()