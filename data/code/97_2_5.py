class TruthTableGenerator:
    def generate(self, a, b, c):
        results = []
        for val_a in [0, 1]:
            for val_b in [0, 1]:
                for val_c in [0, 1]:
                    result = (val_a << 2) + (val_b << 1) + val_c
                    results.append((val_a, val_b, val_c, result))
        return results
    def display(self, results):
        print("A | B | C | A & B & C | A & ~B & C | ~A & B & C | ~A & ~B & C | A & B & ~C | A & ~B & ~C | ~A & B & ~C | ~A & ~B & C | A & ~B & C | ~A & B & C | ~A & ~B & ~C")
        print("-" * 85)
        for a, b, c, r in results:
            print(f"{a} | {b} | {c} | {r}")
if __name__ == '__main__':
    generator = TruthTableGenerator()
    a_val = 0
    b_val = 1
    c_val = 0
    truth_table_data = generator.generate(a_val, b_val, c_val)
    generator.display(truth_table_data)