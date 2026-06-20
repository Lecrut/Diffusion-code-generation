class TruthTableGenerator:
    def generate_truth_table(self):
        headers = ['A', 'B', 'C', 'A AND B', 'A OR B', 'NOT A']
        table = [headers]
        for a in [False, True]:
            for b in [False, True]:
                for c in [False, True]:
                    row = [a, b, c, a and b, a or b, not a]
                    table.append(row)
        return table

    def display_truth_table(self):
        table = self.generate_truth_table()
        for row in table:
            print(' | '.join(str(cell) for cell in row))

if __name__ == '__main__':
    generator = TruthTableGenerator()
    generator.display_truth_table()