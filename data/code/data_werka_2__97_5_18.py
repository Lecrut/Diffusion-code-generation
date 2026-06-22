class TruthTableGenerator:
    def __init__(self, num_inputs, expression_func):
        if not isinstance(num_inputs, int) or num_inputs <= 0:
            raise ValueError("num_inputs must be a positive integer")
        if not callable(expression_func):
            raise ValueError("expression_func must be callable")
        self.num_inputs = num_inputs
        self.expression_func = expression_func
        self.input_names = [chr(ord('A') + i) for i in range(num_inputs)]

    def generate_rows(self):
        total = 1 << self.num_inputs
        rows = []
        for i in range(total):
            inputs = []
            for j in range(self.num_inputs):
                bit = (i >> (self.num_inputs - 1 - j)) & 1
                inputs.append(bool(bit))
            result = self.expression_func(*inputs)
            row = {name: val for name, val in zip(self.input_names, inputs)}
            row['Result'] = result
            rows.append(row)
        return rows

    def display(self):
        rows = self.generate_rows()
        header = ' | '.join(f'{name:<5}' for name in self.input_names) + ' | Result'
        print(header)
        print('-' * len(header))
        for row in rows:
            vals = [str(row[name]) for name in self.input_names]
            print(' | '.join(f'{v:<5}' for v in vals) + f" | {row['Result']}")

def logical_expression(a, b, c, d):
    return (a and b) or (not c and d)

if __name__ == '__main__':
    generator = TruthTableGenerator(4, logical_expression)
    generator.display()