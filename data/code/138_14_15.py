class TruthTable:
    TRUE = True
    FALSE = False

    @staticmethod
    def implies(a, b):
        return not a or b

    @classmethod
    def print_truth_table(cls):
        for p in [cls.TRUE, cls.FALSE]:
            for q in [cls.TRUE, cls.FALSE]:
                result = cls.implies(p, q)
                print(f"P: {p}, Q: {q} -> {result}")

if __name__ == '__main__':
    TruthTable.print_truth_table()