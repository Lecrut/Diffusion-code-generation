class TruthTableGenerator:
    def generate_table(self):
        table = []
        for a in [False, True]:
            for b in [False, True]:
                for c in [False, True]:
                    row = {'A': a, 'B': b, 'C': c}
                    row['A and B'] = a and b
                    row['A or B'] = a or b
                    row['not A'] = not a
                    row['A xor B'] = (a and not b) or (not a and b)
                    table.append(row)
        return table

    def display_table(self, table):
        for row in table:
            print(f"A: {row['A']}, B: {row['B']}, C: {row['C']}, A and B: {row['A and B']}, A or B: {row['A or B']}, not A: {row['not A']}, A xor B: {row['A xor B']}")

if __name__ == '__main__':
    generator = TruthTableGenerator()
    table = generator.generate_table()
    generator.display_table(table)