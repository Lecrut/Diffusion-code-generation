class TruthTableGenerator:
    HEADER_PREFIX = "V"

    @staticmethod
    def generate_truth_table(bool1, bool2):
        truth_table = {
            (bool1, bool2): all((bool1, bool2)),
            (not bool1, bool2): any((not bool1, bool2)),
            (bool1, not bool2): any((bool1, not bool2)),
            (not bool1, not bool2): not any((not bool1, not bool2))
        }
        return truth_table

    @staticmethod
    def print_truth_table(truth_table):
        header = " | ".join([f"{TruthTableGenerator.HEADER_PREFIX}{i+1}" for i in range(2)])
        print(f"Truth Table:")
        print("-" * len(header))
        print(header)
        print("-" * len(header))
        for inputs, result in truth_table.items():
            print(f"{inputs[0]} | {inputs[1]} | {result}")

if __name__ == '__main__':
    sample_truth_table = TruthTableGenerator.generate_truth_table(True, False)
    TruthTableGenerator.print_truth_table(sample_truth_table)