class XORTruthTableGenerator:
    def generate_truth_table(self):
        for p in [True, False]:
            for q in [True, False]:
                yield (p, q, p ^ q)

if __name__ == '__main__':
    generator = XORTruthTableGenerator()
    for p, q, r in generator.generate_truth_table():
        print(f"P={p}, Q={q} => P ^ Q = {r}")