class TruthTableValidator:
    P_VALUES = [0, 1]
    Q_VALUES = [0, 1]

    @staticmethod
    def validate_truth_table():
        print("P | Q | (A and B) OR (not A and not B)")
        print("-" * 40)
        for p in TruthTableValidator.P_VALUES:
            for q in TruthTableValidator.Q_VALUES:
                result = (p and q) or (not p and not q)
                print(f"{p} | {q} | {result}")

if __name__ == '__main__':
    TruthTableValidator.validate_truth_table()