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
        print("P\tQ\tResult")
        for p, q, res in rows:
            print(f"{str(p)}\t{str(q)}\t{str(res)}")

def logical_and(p, q):
    return p and q

if __name__ == '__main__':
    table = TruthTable(logical_and)
    table.display()
    rows = table.generate()
    print(rows)