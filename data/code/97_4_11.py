class BinaryTruthTable:
    def generate_truth_table(self):
        P_values = [False, True]
        Q_values = [False, True]
        table = []
        for p in P_values:
            for q in Q_values:
                row = {'P': p, 'Q': q, 'P OR Q': p or q}
                table.append(row)
        return table

if __name__ == '__main__':
    generator = BinaryTruthTable()
    truth_table = generator.generate_truth_table()
    for row in truth_table:
        print(f"{row['P']} | {row['Q']} | {row['P OR Q']}")