class BinaryTruthTableGenerator:
    def generate_truth_table(self):
        table = []
        for p in [False, True]:
            for q in [False, True]:
                row = {'P': p, 'Q': q, 'P -> Q': not p or q}
                table.append(row)
        return table

if __name__ == '__main__':
    generator = BinaryTruthTableGenerator()
    truth_table = generator.generate_truth_table()
    print("P | Q | P -> Q")
    for row in truth_table:
        print(f"{row['P']} | {row['Q']} | {row['P -> Q']}")