class TruthTableGenerator:
    def generate_table(self):
        headers = ['A', 'B', 'C', 'A AND B', 'A OR B', 'NOT A', 'NOT B', 'NOT C']
        table = [headers]
        
        for a in [False, True]:
            for b in [False, True]:
                for c in [False, True]:
                    row = [
                        a, b, c,
                        a and b, a or b,
                        not a, not b, not c
                    ]
                    table.append(row)
        
        return table

    def print_table(self):
        table = self.generate_table()
        for row in table:
            print(' | '.join(str(cell) for cell in row))

if __name__ == '__main__':
    generator = TruthTableGenerator()
    generator.print_table()