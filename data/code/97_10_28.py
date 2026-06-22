class TruthTable:
    def __init__(self, expr_func):
        self.expr_func = expr_func

    def generate(self):
        rows = []
        header = "A | B | Result"
        separator = "---+---+-------"
        rows.append(header)
        rows.append(separator)
        for a in [False, True]:
            for b in [False, True]:
                result = self.expr_func(a, b)
                a_str = str(a)
                b_str = str(b)
                res_str = str(result)
                row = f"{a_str} | {b_str} | {res_str}"
                rows.append(row)
        return "\n".join(rows)

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
    print(table.generate())
    print()
    table2 = TruthTable(xor_func)
    print(table2.generate())