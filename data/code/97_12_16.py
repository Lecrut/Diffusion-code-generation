class TruthTable:
    def __init__(self):
        self.table = []

    def add_row(self, inputs, output):
        self.table.append((inputs[0], inputs[1], output))

    def generate_table(self):
        for a in [0, 1]:
            for b in [0, 1]:
                output = a ^ b
                self.add_row([a, b], output)

    def display_table(self):
        print(f"{'A':<3} {'B':<3} Output")
        for row in self.table:
            print(f"{row[0]:<3} {row[1]:<3} {row[2]}")

if __name__ == '__main__':
    truth_table = TruthTable()
    truth_table.generate_table()
    truth_table.display_table()