class ImplicationTable:
    def __init__(self):
        self.variables = [False, True]

    def compute(self, p, q):
        if not isinstance(p, bool) or not isinstance(q, bool):
            raise ValueError("Inputs must be boolean")
        return (not p) or q

    def generate_rows(self):
        rows = []
        for p in self.variables:
            for q in self.variables:
                val = self.compute(p, q)
                rows.append((p, q, val))
        return rows

    def format_row(self, p, q, r):
        return f"P={p}, Q={q}, P -> Q={r}"

    def print_all(self):
        rows = self.generate_rows()
        for p, q, r in rows:
            print(self.format_row(p, q, r))

if __name__ == '__main__':
    table = ImplicationTable()
    table.print_all()
    rows = table.generate_rows()
    print(len(rows))