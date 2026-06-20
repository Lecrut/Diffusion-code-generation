class TruthTableGenerator:
    @staticmethod
    def xor_truth_table():
        for p in [True, False]:
            for q in [True, False]:
                yield (p, q, p ^ q)

if __name__ == '__main__':
    generator = TruthTableGenerator()
    for row in generator.xor_truth_table():
        print(f"P={row[0]}, Q={row[1]} => P ^ Q = {row[2]}")