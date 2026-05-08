class TruthTableGenerator:
    def generate_truth_table(self, var1_names, var2_names):
        table = []
        n1 = len(var1_names)
        n2 = len(var2_names)
        for i in range(n1):
            for j in range(n2):
                combination = (var1_names[i], var2_names[j])
                table.append(combination)
        return table
if __name__ == '__main__':
    generator = TruthTableGenerator()
    var1_names = ["A", "B"]
    var2_names = ["X", "Y"]
    truth_table = generator.generate_truth_table(var1_names, var2_names)
    for row in truth_table:
        print(row)