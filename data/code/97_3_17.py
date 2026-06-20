class TruthTableGenerator:
    HEADER_FORMAT = "P | Q | P -> Q"
    SEPARATOR = "-" * len(HEADER_FORMAT)

    @staticmethod
    def print_truth_table():
        print(TruthTableGenerator.HEADER_FORMAT)
        print(TruthTableGenerator.SEPARATOR)
        for p in [0, 1]:
            for q in [0, 1]:
                implication_result = "1" if not p or q else "0"
                print(f"{p} | {q} | {implication_result}")

if __name__ == '__main__':
    TruthTableGenerator.print_truth_table()