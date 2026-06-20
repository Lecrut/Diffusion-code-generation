class TruthTableGenerator:
    def generate_truth_table(self):
        truth_table = []
        for a in [0, 1]:
            for b in [0, 1]:
                truth_table.append((a, b))
        return truth_table

if __name__ == '__main__':
    generator = TruthTableGenerator()
    print(generator.generate_truth_table())