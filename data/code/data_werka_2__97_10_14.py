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
        col_widths = [max(len(str(row[i])) for row in rows) for i in range(3)]
        header_fmt = ' | '.join('{:>' + str(w) + '}' for w in col_widths)
        separator = '-+-'.join('-' * w for w in col_widths)
        print(header_fmt.format(*rows[0]))
        print(separator)
        for row in rows[1:]:
            print(header_fmt.format(*row))

def logical_and(a, b):
    return a and b

def logical_or(a, b):
    return a or b

def logical_xor(a, b):
    return a != b

if __name__ == '__main__':
    table = TruthTable(logical_and)
    table.display()
    print()
    table_or = TruthTable(logical_or)
    table_or.display()
    print()
    table_xor = TruthTable(logical_xor)
    table_xor.display()