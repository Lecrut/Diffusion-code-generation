class TruthTableGenerator:
    def generate_truth_table(self, var1_names, var2_names):
        table = []
        for v1 in [0, 1]:
            for v2 in [0, 1]:
                table.append((v1, v2))
        return table
if __name__ == '__main__':
    generator = TruthTableGenerator()
    var1_names = ["A", "B"]
    var2_names = ["X", "Y"]
    combinations = generator.generate_truth_table(var1_names, var2_names)
    for combo in combinations:
        print(f"{var1_names[0]}: {combo[0]}, {var1_names[1]}: {combo[1]}")