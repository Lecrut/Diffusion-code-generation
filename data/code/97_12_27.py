class XorTruthTable:
    INPUTS = [0, 1]

    def __init__(self):
        self.table = []
        self._build_table()

    def _build_table(self):
        for a in self.INPUTS:
            for b in self.INPUTS:
                self.table.append((a, b, a ^ b))

    def get_table(self):
        return self.table

if __name__ == '__main__':
    table_generator = XorTruthTable()
    rows = table_generator.get_table()
    for row in rows:
        print(row)