class TruthTableGenerator:
    def generate_truth_table(self):
        table = []
        P_values = [False, True]
        Q_values = [False, True]
        for p in P_values:
            for q in Q_values:
                row = {'P': p, 'Q': q}
                row['P AND Q'] = p and q
                row['P OR Q'] = p or q
                row['NOT P'] = not p
                row['NOT Q'] = not q
                table.append(row)
        return table

if __name__ == '__main__':
    generator = TruthTableGenerator()
    truth_table = generator.generate_truth_table()
    for row in truth_table:
        print(row)