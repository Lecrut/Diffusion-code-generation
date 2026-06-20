class TruthTableGenerator:
    VARIABLES = ["A", "B", "C", "D"]
    VALUES = [0, 1]

    @staticmethod
    def generate_truth_table():
        table = []
        for v1 in TruthTableGenerator.VALUES:
            for v2 in TruthTableGenerator.VALUES:
                for v3 in TruthTableGenerator.VALUES:
                    for v4 in TruthTableGenerator.VALUES:
                        row = [v1, v2, v3, v4]
                        table.append(row)
        return table

if __name__ == '__main__':
    generator = TruthTableGenerator()
    truth_table = generator.generate_truth_table()
    for row in truth_table:
        print(f"{TruthTableGenerator.VARIABLES[0]}: {row[0]}, {TruthTableGenerator.VARIABLES[1]}: {row[1]}, {TruthTableGenerator.VARIABLES[2]}: {row[2]}, {TruthTableGenerator.VARIABLES[3]}: {row[3]}")