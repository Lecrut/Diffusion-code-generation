class BooleanTableGenerator:
    TRUE = True
    FALSE = False

    @staticmethod
    def implication(a, b):
        return not a or b

    @staticmethod
    def equivalence(a, b):
        return a == b

    @classmethod
    def generate_truth_tables(cls):
        results = []
        for a in [cls.TRUE, cls.FALSE]:
            for b in [cls.TRUE, cls.FALSE]:
                implication_result = cls.implication(a, b)
                equivalence_result = cls.equivalence(a, b)
                results.append((a, b, implication_result, equivalence_result))
        return results

if __name__ == '__main__':
    truth_tables = BooleanTableGenerator.generate_truth_tables()
    for row in truth_tables:
        print(row)