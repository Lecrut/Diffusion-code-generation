class TruthTableGenerator:
    @staticmethod
    def generate_truth_table(a, b):
        results = [
            (a, b),
            (a, not b),
            (not a, b),
            (not a, not b)
        ]
        return tuple(results)

    @staticmethod
    def bitwise_operations(truth_table):
        and_results = [(x[0] and x[1]) for x in truth_table]
        or_results = [(x[0] or x[1]) for x in truth_table]
        xor_results = [((x[0] and not x[1]) or (not x[0] and x[1])) for x in truth_table]
        return zip(truth_table, and_results, or_results, xor_results)

if __name__ == '__main__':
    a_val = True
    b_val = False
    truth_table = TruthTableGenerator.generate_truth_table(a_val, b_val)
    operation_results = TruthTableGenerator.bitwise_operations(truth_table)
    print(operation_results)