class TruthTable:
    def __init__(self, expr_func):
        self.expr_func = expr_func

    def generate(self):
        rows = []
        headers = ['A', 'B', 'Result']
        rows.append(headers)
        for a in [False, True]:
            for b in [False, True]:
                result = self.expr_func(a, b)
                rows.append([a, b, result])
        return rows

    def display(self):
        rows = self.generate()
        col_widths = [4, 4, 8]
        header = [str(h).ljust(col_widths[i]) for i, h in enumerate(rows[0])]
        print(' '.join(header))
        print('-' * len(' '.join(header)))
        for row in rows[1:]:
            formatted_row = [str(val).ljust(col_widths[i]) for i, val in enumerate(row)]
            print(' '.join(formatted_row))

def and_func(a, b):
    return a and b

def or_func(a, b):
    return a or b

def nand_func(a, b):
    return not (a and b)

def xor_func(a, b):
    return a ^ b

if __name__ == '__main__':
    table = TruthTable(xor_func)
    table.display()