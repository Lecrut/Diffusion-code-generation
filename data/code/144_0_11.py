class TruthTableGenerator:
    A = True
    B = False
    C = True

    @staticmethod
    def logical_expression(A, B, C):
        return (A and B) or not C

    def generate_truth_table(self):
        truth_table = []
        truth_table.append([self.A, self.B, self.C, self.logical_expression(self.A, self.B, self.C)])
        return truth_table

if __name__ == '__main__':
    generator = TruthTableGenerator()
    table = generator.generate_truth_table()
    print(table)