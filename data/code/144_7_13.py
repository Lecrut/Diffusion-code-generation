import itertools

class TruthTableBuilder:
    def __init__(self, variables):
        self.variables = variables
        self.n = len(variables)
    
    def build_truth_table(self):
        results = []
        for combination in itertools.product([False, True], repeat=self.n):
            row = {var: val for var, val in zip(self.variables, combination)}
            results.append(row)
        return results

if __name__ == '__main__':
    builder = TruthTableBuilder(["A", "B"])
    truth_table = builder.build_truth_table()
    
    print("Truth Table for A and B:")
    header = " | ".join(builder.variables)
    print(header)
    print("-" * len(header))
    for combination in truth_table:
        row = " | ".join(str(combination[var]) for var in builder.variables)
        print(row)