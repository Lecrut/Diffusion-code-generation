class TruthTableGenerator:
    def generate_table(self):
        table = []
        for a in [False, True]:
            for b in [False, True]:
                for c in [False, True]:
                    row = {'A': a, 'B': b, 'C': c}
                    row['A AND B'] = a and b
                    row['A OR B'] = a or b
                    row['NOT A'] = not a
                    row['A XOR B'] = a != b
                    table.append(row)
        return table

    def display_table(self):
        table = self.generate_table()
        headers = ['A', 'B', 'C', 'A AND B', 'A OR B', 'NOT A', 'A XOR B']
        print('\t'.join(headers))
        for row in table:
            print('\t'.join(str(row[col]) for col in headers))

if __name__ == '__main__':
    generator = TruthTableGenerator()
    generator.display_table()