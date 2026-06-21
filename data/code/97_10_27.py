class TruthTable:
    def __init__(self, expression_func):
        self.expression_func = expression_func

    def generate(self):
        rows = []
        headers = ['A', 'B', 'Result']
        rows.append(headers)
        for a in [False, True]:
            for b in [False, True]:
                result = self.expression_func(a, b)
                rows.append([a, b, result])
        return rows

    def display(self):
        rows = self.generate()
        col_widths = [max(len(str(row[i])) for row in rows) for i in range(3)]
        header_fmt = ' | '.join(f'{{:<{w}}}' for w in col_widths)
        separator = '-+-'.join('-' * w for w in col_widths)
        print(header_fmt.format(*rows[0]))
        print(separator)
        for row in rows[1:]:
            print(header_fmt.format(*row))

def and_expr(a, b):
    return a and b

def or_expr(a, b):
    return a or b

def nand_expr(a, b):
    return not (a and b)

def xor_expr(a, b):
    return a ^ b

if __name__ == '__main__':
    table = TruthTable(xor_expr)
    table.display()