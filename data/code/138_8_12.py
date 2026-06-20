class TruthTableValidator:
    P_VALUES = [0, 1]
    Q_VALUES = [0, 1]

    @staticmethod
    def validate_truth_table():
        print("P | Q | (A AND B) OR (NOT A AND NOT B)")
        print("-" * 40)
        for p in TruthTableValidator.P_VALUES:
            for q in TruthTableValidator.Q_VALUES:
                a_and_b = p and q
                not_a_and_not_b = not p and not q
                result = a_and_b or not_a_and_not_b
                print(f"{p} | {q} | {result}")

if __name__ == '__main__':
    validator = TruthTableValidator()
    validator.validate_truth_table()