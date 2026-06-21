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
        header_fmt = ' | '.join('{:<{w}}' for w in col_widths)
        separator = '-+-'.join('-' * w for w in col_widths)
        row_fmt = ' | '.join('{:<{w}}' for w in col_widths)

        print(header_fmt.format(*rows[0], **{f'w{i}': col_widths[i] for i in range(3)}))
        print(separator)
        for row in rows[1:]:
            print(row_fmt.format(*row, **{f'w{i}': col_widths[i] for i in range(3)}))

def and_func(a, b):
    return a and b

def or_func(a, b):
    return a or b

def nand_func(a, b):
    return not (a and b)

if __name__ == '__main__':
    table = TruthTable(and_func)
    table.display()
    print()
    table2 = TruthTable(or_func)
    table2.display()
    print()
    table3 = TruthTable(nand_func)
    table3.display()