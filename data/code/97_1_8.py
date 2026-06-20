class TruthTableGenerator:
    def generate_truth_table(self):
        for a in [False, True]:
            for b in [False, True]:
                for c in [False, True]:
                    print(f"A: {a}, B: {b}, C: {c}")

if __name__ == '__main__':
    generator = TruthTableGenerator()
    generator.generate_truth_table()