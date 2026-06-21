class ImplicationTruthTable:
    def __init__(self):
        self.table = []

    def generate_table(self):
        for P in [True, False]:
            for Q in [True, False]:
                result = "T" if not P or Q else "F"
                self.table.append((P, Q, result))

    def print_table(self):
        for row in self.table:
            print(f"{row[0]:<5}{row[1]:<5}{row[2]}")

if __name__ == '__main__':
    tt = ImplicationTruthTable()
    tt.generate_table()
    tt.print_table()