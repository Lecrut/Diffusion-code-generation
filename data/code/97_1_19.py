TRUTH_TABLE_HEADERS = ['A', 'B', 'C']
TRUTH_VALUES = [False, True]

class TruthTableGenerator:
    def generate_truth_table(self):
        header = '|'.join(TRUTH_TABLE_HEADERS)
        separator = '-' * len(header)
        print(separator)
        print(header)
        print(separator)
        for a in TRUTH_VALUES:
            for b in TRUTH_VALUES:
                for c in TRUTH_VALUES:
                    row = '|'.join([str(a), str(b), str(c)])
                    print(row)
                    print(separator)

if __name__ == '__main__':
    generator = TruthTableGenerator()
    generator.generate_truth_table()