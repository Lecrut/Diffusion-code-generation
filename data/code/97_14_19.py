class TruthTableGenerator:
    INPUT_VALUES = [True, False]

    @staticmethod
    def generate_or_truth_table():
        results = []
        for a in TruthTableGenerator.INPUT_VALUES:
            for b in TruthTableGenerator.INPUT_VALUES:
                or_result = a or b
                results.append({'a': a, 'b': b, 'or_result': or_result})
        return results

if __name__ == '__main__':
    truth_table = TruthTableGenerator.generate_or_truth_table()
    print("A | B | A OR B")
    print("---|---|--------")
    for row in truth_table:
        print(f"{row['a']} | {row['b']} | {row['or_result']}")