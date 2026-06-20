class TruthTableGenerator:
    @staticmethod
    def xor_truth_table():
        for p in [True, False]:
            for q in [True, False]:
                yield (p, q, p ^ q)

if __name__ == '__main__':
    generator = TruthTableGenerator()
    for p, q, r in generator.xor_truth_table():
        print(f"P={p}, Q={q} => P XOR Q = {r}")