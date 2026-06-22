class TruthTableGenerator:
    def __init__(self, variable_names=None, num_vars=0):
        if variable_names is not None:
            self.variables = list(variable_names)
        else:
            self.variables = [f"var{i}" for i in range(num_vars)]
        self.num_vars = len(self.variables)
        self.operator_map = {
            'AND': lambda a, b: a and b,
            'OR': lambda a, b: a or b,
            'NAND': lambda a, b: not (a and b),
            'NOR': lambda a, b: not (a or b),
            'XOR': lambda a, b: a ^ b,
            'IMPLIES': lambda a, b: (not a) or b,
            'EQUIV': lambda a, b: a == b,
        }
        self.expression = None
        self.result_col = "Result"

    def set_expression(self, expr):
        self.expression = expr

    def _get_bits(self, index):
        bits = []
        for i in range(self.num_vars - 1, -1, -1):
            bit = (index >> i) & 1
            bits.append(bool(bit))
        return bits

    def _evaluate_expression(self, values):
        if self.expression is None:
            return None
        context = dict(zip(self.variables, values))
        try:
            result = eval(self.expression, {"__builtins__": {}}, context)
            return bool(result)
        except Exception:
            return None

    def generate(self):
        headers = list(self.variables) + [self.result_col]
        total_rows = 2 ** self.num_vars
        table = []
        for i in range(total_rows):
            values = self._get_bits(i)
            row = values + [self._evaluate_expression(values)]
            table.append(row)
        return headers, table

if __name__ == '__main__':
    generator = TruthTableGenerator(variable_names=['P', 'Q'])
    generator.set_expression('P and Q')
    headers, table = generator.generate()
    print(headers)
    for row in table:
        print(row)