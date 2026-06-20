class TruthTableGenerator:
    INPUT_VALUES = [True, False]

    @staticmethod
    def generate_or_truth_table():
        results = []
        for a in TruthTableGenerator.INPUT_VALUES:
            for b in TruthTableGenerator.INPUT_VALUES:
                or_result = a or b
                results.append({'a': a, 'b': b, 'a OR b': or_result})
        return results

if __name__ == '__main__':
    truth_table = TruthTableGenerator.generate_or_truth_table()
    print("a | b | a OR b")
    print("---|---|---------")
    for row in truth_table:
        print(f"{row['a']} | {row['b']} | {row['a OR b']}")