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
        col_widths = [max(len(str(row[i])) for row in rows) for i in range(len(rows[0]))]
        header = " | ".join(str(h).ljust(col_widths[i]) for i, h in enumerate(rows[0]))
        separator = "-+-".join("-" * w for w in col_widths)
        print(header)
        print(separator)
        for row in rows[1:]:
            line = " | ".join(str(val).ljust(col_widths[i]) for i, val in enumerate(row))
            print(line)

def and_expr(a, b):
    return a and b

def or_expr(a, b):
    return a or b

def nand_expr(a, b):
    return not (a and b)

if __name__ == '__main__':
    table = TruthTable(and_expr)
    table.display()
    print()
    table2 = TruthTable(or_expr)
    table2.display()
    print()
    table3 = TruthTable(nand_expr)
    table3.display()