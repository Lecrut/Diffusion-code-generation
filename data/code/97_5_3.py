class TruthTableGenerator:
    def generate_truth_table(self, var1_names, var2_names):
        combinations = []
        for v1 in [0, 1]:
            for v2 in [0, 1]:
                combinations.append((v1, v2))
        header = [var1_names[0], var2_names[0]]
        table_rows = [header]
        for v1, v2 in combinations:
            row = [str(v1), str(v2)]
            table_rows.append(row)
        return table_rows
if __name__ == '__main__':
    generator = TruthTableGenerator()
    var1_names = ["A", "B"]
    var2_names = ["X", "Y"]
    truth_table = generator.generate_truth_table(var1_names, var2_names)
    print("Variable Combinations:")
    print(truth_table[0])
    for row in truth_table[1:]:
        print(row)