class BinaryTruthTable:
    def __init__(self):
        self.variables = ['A', 'B']

    def _validate_input(self, var_list):
        if not isinstance(var_list, list) or len(var_list) != 2:
            raise ValueError("Expected a list of exactly 2 variable names")
        for var in var_list:
            if not isinstance(var, str):
                raise ValueError("Variable names must be strings")

    def generate_table(self, vars=None):
        if vars is None:
            vars = self.variables
        self._validate_input(vars)
        
        table = []
        for i in range(4):
            row = []
            val_a = (i >> 1) & 1
            val_b = i & 1
            row.append({vars[0]: val_a, vars[1]: val_b})
            table.append(row[0])
        return table

if __name__ == '__main__':
    tt = BinaryTruthTable()
    print(tt.generate_table())