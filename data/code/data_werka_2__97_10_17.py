class TruthTable:
    def __init__(self, expr_func):
        self.expr_func = expr_func

    def generate(self):
        rows = []
        headers = ["A", "B", "Result"]
        rows.append(headers)
        for a in [False, True]:
            for b in [False, True]:
                result = self.expr_func(a, b)
                rows.append([a, b, result])
        return rows

    def display(self):
        rows = self.generate()
        col_widths = [4, 4, 8]
        header_line = " | ".join(h.center(col_widths[i]) for i, h in enumerate(rows[0]))
        separator = "-+-".join("-" * w for w in col_widths)
        print(header_line)
        print(separator)
        for row in rows[1:]:
            line = " | ".join(str(val).center(col_widths[i]) for i, val in enumerate(row))
            print(line)

def and_func(a, b):
    return a and b

def or_func(a, b):
    return a or b

def nand_func(a, b):
    return not (a and b)

def xor_func(a, b):
    return a ^ b

if __name__ == '__main__':
    table = TruthTable(and_func)
    table.display()
    print()
    table2 = TruthTable(xor_func)
    table2.display()