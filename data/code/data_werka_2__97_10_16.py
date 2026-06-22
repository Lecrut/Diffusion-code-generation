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
        header_format = ' | '.join('{:<' + str(w) + '}' for w in col_widths)
        separator = '-+-'.join('-' * w for w in col_widths)
        print(header_format.format(*rows[0]))
        print(separator)
        for row in rows[1:]:
            print(header_format.format(*[str(x) for x in row]))

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
    table2 = TruthTable(or_func)
    table2.display()
    print()
    table3 = TruthTable(nand_func)
    table3.display()
    print()
    table4 = TruthTable(xor_func)
    table4.display()