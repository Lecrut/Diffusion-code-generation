class TruthTableGenerator:
    VAR_NAMES = ["A", "B", "C", "D"]
    
    @staticmethod
    def generate_truth_table():
        table = []
        for v1 in [0, 1]:
            for v2 in [0, 1]:
                for v3 in [0, 1]:
                    for v4 in [0, 1]:
                        table.append((v1, v2, v3, v4))
        return table
    
    @staticmethod
    def print_truth_table(table):
        header = TruthTableGenerator.VAR_NAMES
        print(f"{header[0]} | {header[1]} | {header[2]} | {header[3]}")
        for row in table:
            print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]}")

if __name__ == '__main__':
    generator = TruthTableGenerator()
    truth_table = generator.generate_truth_table()
    generator.print_truth_table(truth_table)