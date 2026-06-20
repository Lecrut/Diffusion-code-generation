class TruthTableGenerator:
    def generate_table(self):
        header = ['A', 'B', 'C', 'A AND B', 'A OR B', 'NOT A']
        table = [header]
        for a in [False, True]:
            for b in [False, True]:
                for c in [False, True]:
                    row = [a, b, c, a and b, a or b, not a]
                    table.append(row)
        return table

    def print_table(self):
        table = self.generate_table()
        for row in table:
            print(row)

if __name__ == '__main__':
    generator = TruthTableGenerator()
    generator.print_table()