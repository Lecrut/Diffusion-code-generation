class TruthTableGenerator:
    HEADER = "P | Q | P AND Q"
    DELIMITER = "---|---|---------"

    @staticmethod
    def generate_truth_table():
        print(TruthTableGenerator.HEADER)
        print(TruthTableGenerator.DELIMITER)
        for p in [True, False]:
            for q in [True, False]:
                result = p and q
                print(f"{p} | {q} | {result}")

if __name__ == '__main__':
    TruthTableGenerator.generate_truth_table()