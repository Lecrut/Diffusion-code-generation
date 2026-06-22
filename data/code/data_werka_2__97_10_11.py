class TruthTable:
    def __init__(self, expr_func):
        self.expr_func = expr_func

    def generate(self):
        rows = []
        for p in [False, True]:
            for q in [False, True]:
                result = self.expr_func(p, q)
                rows.append((p, q, result))
        return rows

    def display(self):
        rows = self.generate()
        print(f"{'P':<5} {'Q':<5} {'Result':<7}")
        print("-" * 20)
        for p, q, res in rows:
            print(f"{str(p):<5} {str(q):<5} {str(res):<7}")

def and_func(p, q):
    return p and q

def or_func(p, q):
    return p or q

def nand_func(p, q):
    return not (p and q)

if __name__ == '__main__':
    table = TruthTable(and_func)
    table.display()
    print()
    table2 = TruthTable(or_func)
    table2.display()
    print()
    table3 = TruthTable(nand_func)
    table3.display()