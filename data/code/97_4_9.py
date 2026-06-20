class BinaryTruthTable:
    TRUE = True
    FALSE = False
    
    def __init__(self):
        self.columns = ["P", "Q", "P -> Q"]
    
    def generate_truth_table(self):
        results = []
        for p in [self.TRUE, self.FALSE]:
            for q in [self.TRUE, self.FALSE]:
                result = not p or q
                row = [p, q, result]
                results.append(row)
        return results
    
    def print_truth_table(self):
        print(" | ".join(self.columns))
        for row in self.generate_truth_table():
            print(" | ".join(str(cell) for cell in row))

if __name__ == '__main__':
    generator = BinaryTruthTable()
    generator.print_truth_table()