class TruthTableGenerator:
    def generate_truth_table(self):
        truth_values = [False, True]
        print("P | Q | P -> Q")
        for p in truth_values:
            for q in truth_values:
                result = not p or q
                print(f"{p} | {q} | {result}")

if __name__ == '__main__':
    generator = TruthTableGenerator()
    generator.generate_truth_table()