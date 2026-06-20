class TruthTableGenerator:
    def generate_truth_table(self):
        return [
            (0, 0, 0),
            (0, 1, 1),
            (1, 0, 1),
            (1, 1, 0)
        ]

if __name__ == '__main__':
    generator = TruthTableGenerator()
    print(generator.generate_truth_table())