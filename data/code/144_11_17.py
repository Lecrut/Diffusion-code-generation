class TruthTableGenerator:
    @staticmethod
    def generate_truth_table():
        return [
            (True, True, False),
            (True, False, False),
            (False, True, True),
            (False, False, True)
        ]

if __name__ == '__main__':
    table = TruthTableGenerator.generate_truth_table()
    for row in table:
        print(row)